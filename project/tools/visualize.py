import argparse
import os
import sys
import json

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description='Visualize training statistics.')
    parser.add_argument('train_log', type=str,
                        help='The training.log file to visualize.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    dir_name = os.path.split(args.train_log)[0]

    # Get statistics
    dis_loss = []
    nn_prec = []
    csls_prec = []
    dis_src_pred = []
    dis_tgt_pred = []
    dis_accu = []
    with open(args.train_log, 'r') as fin:
        for line in fin:
            if 'Starting adversarial training' in line:
                dis_loss.append([])
            elif '__log__' in line:
                log_dict_s = line[line.find('__log__:') + 8:]
                log_dict = json.loads(log_dict_s)
                if 'dis_src_pred' in log_dict: # not refinement
                    nn_prec += [(log_dict['precision_at_1-nn'], log_dict['precision_at_5-nn'], log_dict['precision_at_10-nn'])]
                    csls_prec += [(log_dict['precision_at_1-csls_knn_10'], log_dict['precision_at_5-csls_knn_10'], log_dict['precision_at_10-csls_knn_10'])]
                    dis_src_pred += [log_dict['dis_src_pred']]
                    dis_tgt_pred += [log_dict['dis_tgt_pred']]
                    dis_accu += [log_dict['dis_accu']]
            elif 'Discriminator loss' in line:
                loss_i = line.find('loss')
                dis_loss[-1] += [float(line[loss_i+6:loss_i+12])]

    # Discriminator loss & accuracy
    epochs = len(dis_loss)
    iters = len(dis_loss[0])
    all_dis_loss = [l for dl in dis_loss for l in dl]
    all_dis_accu = [dis_accu[(i - iters // 2) // iters]
                        if (i >= iters // 2) and ((i - iters // 2) % iters == 0) else None
                        for i in range(epochs * iters)]

    fig, ax1 = plt.subplots(figsize=(10, 3))
    ax2 = ax1.twinx()

    ax1.plot(all_dis_loss, color='b')
    ax1.set_xlabel('epoch')
    ax1.set_xticks(np.arange(iters, (epochs + 1) * iters, step=iters))
    ax1.set_xticklabels(np.arange(1, epochs + 1))
    ax1.set_ylabel('loss', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    ax2.plot(all_dis_accu, 'ro')
    ax2.set_ylabel('Accuracy', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title('Discriminator Training Loss & Accuracy')
    fig.tight_layout()

    filename = os.path.join(dir_name, 'dis_loss_acc.png')
    plt.savefig(filename)
    plt.close()

    # Precision
    fig, ax = plt.subplots(figsize=(10, 3))

    linestyles = ['-', '--', ':']
    for i, k in enumerate([1, 5, 10]):
        nn_prec_k = [p[i] for p in nn_prec]
        csls_prec_k = [p[i] for p in csls_prec]
        ax.plot(nn_prec_k, color='b', linestyle=linestyles[i], label='NN p@{}'.format(k))
        ax.plot(csls_prec_k, color='r', linestyle=linestyles[i], label='CSLS p@{}'.format(k))
    ax.set_xticks(np.arange(epochs))
    ax.set_xticklabels(np.arange(1, epochs + 1))
    ax.set_xlabel('epoch')
    ax.set_ylabel('precision')

    plt.title('NN / CSLS Precision@k')
    plt.legend()
    fig.tight_layout()

    filename = os.path.join(dir_name, 'precision.png')
    plt.savefig(filename)
    plt.close()

    # Prediction
    fig, ax = plt.subplots(figsize=(10, 3))

    ax.plot(dis_src_pred, color='b', label='Source prediction')
    ax.plot(dis_tgt_pred, color='r', label='Target prediction')
    ax.set_xticks(np.arange(epochs))
    ax.set_xticklabels(np.arange(1, epochs + 1))
    ax.set_xlabel('epoch')
    ax.set_ylabel('prediction')

    plt.title('Source / Target Predictions')
    plt.legend()
    fig.tight_layout()

    filename = os.path.join(dir_name, 'prediction.png')
    plt.savefig(filename)
    plt.close()

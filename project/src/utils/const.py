CATS = [
    'cs', 'eess', 'econ', 'math', 'physics', 'q-bio', 'q-fin', 'stat',
    'physics:astro-ph', 'physics:cond-mat', 'physics:gr-qc', 'physics:hep-ex',
    'physics:hep-lat', 'physics:hep-ph', 'physics:hep-th', 'physics:math-ph',
    'physics:nlin', 'physics:nucl-ex', 'physics:nucl-th', 'physics:physics',
    'physics:quant-ph',
]

INSTITUTE_NAMES = {
    'zh': [
        # https://en.wikipedia.org/wiki/List_of_universities_in_China
        'peking university', 'tsinghua university', 'renmin university of china', 'beijing normal university', 'beihang university', 'beijing institute of technology', 'china agricultural university', 'nankai university', 'tianjin university', 'harbin institute of technology'
        'jilin university', 'dalian university of technology', 'university of science and technology of china', 'xiamen university', 'nanjing university', 'southeast university', 'shandong university', 'ocean university of china', 'fudan university', 'shanghai jiao tong university'
        'tongji university', 'east china normal university', 'zhejiang university', 'sun yat-sen university', 'south china university of technology', 'wuhan university', 'huazhong university of science and technology', 'hunan university', 'central south university', 'northwestern polytechnical university'
        'xi\'an jiaotong university', 'lanzhou university', 'chongqing university', 'sichuan university', 'university of electronic science and technology of china', 'anhui university', 'beijing university of technology', 'beijing foreign studies university', 'beijing forestry university', 'beilin university'
        'beijing institute of technology', 'beijing jiaotong university', 'beijing normal university', 'beijing sport university', 'beihang university', 'beijing university of aeronautics and astronautics', 'beijing university of chemical technology', 'beijing university of chinese medicine', 'beijing university of posts and telecommunications', 'beijing university of technology'
        'central china normal university', 'central conservatory of music', 'central south university', 'central university of finance and economics', 'chang\'an university', 'china agricultural university', 'china pharmaceutical university', 'china university of geosciences', 'china university of geosciences', 'china university of mining and technology'
        'china university of mining and technology', 'china university of petroleum', 'china university of petroleum', 'china university of political science and law', 'chongqing university', 'communication university of china', 'dalian maritime university', 'dalian university of technology', 'donghua university', 'east china normal university'
        'east china university of science and technology', 'fourth military medical university', 'fudan university', 'fuzhou university', 'guangxi university', 'guizhou university', 'hainan university', 'harbin engineering university', 'harbin institute of technology', 'hebei university of technology'
        'hefei university of technology', 'hohai university', 'huazhong agricultural university', 'huazhong university of science and technology', 'hunan normal university', 'hunan university', 'inner mongolia university', 'jinan university', 'jiangnan university', 'jilin university'
        'lanzhou university', 'liaoning university', 'minzu university of china', 'the central university for nationalities', 'nanchang university', 'nanjing agricultural university', 'nanjing normal university', 'nanjing university', 'nanjing university of aeronautics and astronautics', 'nanjing university of science and technology'
        'nankai university', 'ningxia university', 'national university of defense technology', 'north china electric power university', 'northeast agricultural university', 'northeast forestry university', 'northeast normal university', 'northeastern university', 'northwest a&f university', 'northwest university'
        'northwestern polytechnical university', 'ocean university of china', 'peking university', 'qinghai university', 'renmin university of china', 'second military medical university', 'shaanxi normal university', 'shandong university', 'shanghai international studies university', 'shanghai jiao tong university'
        'shanghai university', 'shanghai university of finance and economics', 'shihezi university', 'sichuan agricultural university', 'sichuan university', 'south china normal university', 'south china university of technology', 'southeast university', 'southwest university', 'southwest jiaotong university'
        'southwestern university of finance and economics', 'sun yat-sen university', 'soochow university', 'taiyuan university of technology', 'tianjin medical university', 'tianjin university', 'tibet university', 'tongji university', 'tsinghua university', 'university of electronic science and technology of china'
        'beijing university of international business and economics', 'university of science and technology beijing', 'university of science and technology of china', 'wuhan university', 'wuhan university of technology', 'xiamen university', 'xi\'an jiaotong university', 'xidian university', 'xinjiang university', 'yanbian university'
        'yunnan university', 'zhejiang university', 'zhengzhou university', 'zhongnan university of economics and law'
        # https://www.4icu.org/tw/
        'national taiwan university', 'national chiao tung university', 'national tsing hua university', 'national cheng kung university', 'national taiwan normal university', 'tamkang university', 'national chengchi university', 'national central university', 'national sun yat-sen university', 'national chung hsing university'
        'fu jen catholic university', 'ming chuan university', 'national taiwan university of science and technology', 'national yang-ming university', 'tunghai university', 'chinese culture university', 'national chung cheng university', 'soochow university, taiwan', 'chung yuan christian university', 'national taiwan ocean university'
    ],
    'en': [
        # https://www.4icu.org/top-universities-north-america/
        'massachusetts institute of technology', 'harvard university', 'stanford university', 'university of california, berkeley', 'university of michigan', 'university of washington', 'cornell university', 'purdue university', 'university of wisconsin-madison', 'columbia university in the city of new york'
        'university of california, los angeles', 'the university of texas at austin', 'penn state university', 'university of illinois at urbana-champaign', 'university of minnesota', 'new york university', 'university of toronto', 'university of pennsylvania', 'university of southern california', 'the university of british columbia'
        'carnegie mellon university', 'princeton university', 'university of california, irvine', 'university of california, san diego', 'yale university', 'arizona state university', 'university of chicago', 'university of colorado boulder', 'university of north carolina at chapel hill', 'michigan state university'
        'university of california, davis', 'university of florida', 'university of maryland', 'duke university', 'rutgers, the state university of new jersey', 'boston university', 'the university of arizona', 'johns hopkins university', 'northwestern university', 'university of virginia'
        'georgia institute of technology', 'texas a&m university', 'the university of utah', 'the ohio state university', 'north carolina state university', 'mcgill university', 'university of pittsburgh', 'virginia polytechnic institute and state university', 'university of california, santa barbara', 'washington university in st. louis'
        'iowa state university of science and technology', 'tufts university', 'georgia state university', 'indiana university bloomington', 'oregon state university', 'simon fraser university', 'university of massachusetts amherst', 'california institute of technology', 'university of alberta', 'university of waterloo'
        'university of iowa', 'university of georgia', 'brigham young university', 'florida state university', 'university of nebraska-lincoln', 'university of houston', 'university of california, santa cruz', 'colorado state university', 'university of oregon', 'georgetown university'
        'university of delaware', 'george mason university', 'university of south florida', 'university of central florida', 'vanderbilt university', 'brown university', 'washington state university', 'george washington university', 'university at buffalo, state university of new york', 'university of rochester'
        'university of notre dame', 'university of calgary', 'rice university', 'dartmouth college', 'western university', 'york university', 'university of connecticut', 'queen\'s university', 'university of kansas', 'university of california, san francisco'
        'emory university', 'university of illinois at chicago', 'university of california, riverside', 'temple university', 'rochester institute of technology', 'university of kentucky', 'san diego state university', 'university of victoria', 'university of missouri', 'university of cincinnati'
        'the university of tennessee, knoxville', 'university of miami', 'university of south carolina', 'university of north texas', 'virginia commonwealth university', 'the university of oklahoma', 'university of new mexico', 'drexel university', 'rensselaer polytechnic institute', 'northeastern university'
        'san josé state university', 'carleton university', 'boston college', 'university of ottawa', 'mcmaster university', 'university of vermont', 'louisiana state university', 'ryerson university', 'portland state university', 'université de montréal'
        'florida international university', 'the university of texas at dallas', 'case western reserve university', 'california state university, fullerton', 'california state university, northridge', 'kent state university', 'san francisco state university', 'clemson university', 'university of new hampshire', 'university of guelph'
        'oklahoma state university', 'concordia university', 'wayne state university', 'the university of alabama', 'fordham university', 'université laval', 'the university of tennessee at martin', 'stony brook university', 'california polytechnic state university, san luis obispo', 'auburn university'
        'loyola university chicago', 'liberty university', 'michigan technological university', 'depaul university', 'american university', 'university of saskatchewan', 'syracuse university', 'west virginia university', 'utah state university', 'texas tech university'
        'dalhousie university', 'tulane university', 'university of maryland, baltimore county', 'memorial university of newfoundland', 'western michigan university', 'southern methodist university', 'montana state university', 'university of arkansas', 'the university of texas at arlington', 'university of wisconsin-milwaukee'
        'university of denver', 'northern arizona university', 'university of manitoba', 'baylor university', 'university at albany, state university of new york', 'lamar university', 'ohio university', 'university of alabama at birmingham', 'james madison university', 'college of william & mary'
        'california state university, long beach', 'kansas state university', 'university of rhode island', 'santa clara university', 'brandeis university', 'university of idaho', 'northern illinois university', 'grand canyon university', 'florida atlantic university', 'worcester polytechnic institute'
        'indiana university - purdue university indianapolis', 'old dominion university', 'the new school', 'illinois institute of technology', 'mississippi state university', 'university of north carolina at charlotte', 'université du québec à montréal', 'southern new hampshire university', 'binghamton university, state university of new york', 'university of maryland university college'
        'saint louis university', 'university of nevada, las vegas', 'texas state university', 'university of colorado denver', 'university of nevada, reno', 'new mexico state university', 'wake forest university', 'california state university, sacramento', 'california state polytechnic university, pomona', 'lehigh university',
        # https://www.4icu.org/gb/
        'university of oxford', 'university of cambridge', 'university college london', 'the university of edinburgh', 'the university of manchester', 'the university of nottingham', 'the london school of economics and political science', 'university of glasgow', 'university of leeds', 'the university of warwick'
        'imperial college london', 'king\'s college london', 'newcastle university', 'university of southampton', 'university of birmingham', 'the university of sheffield', 'the university of york', 'university of liverpool', 'university of leicester', 'queen mary university of london'
        'durham university', 'university of exeter', 'university of sussex', 'lancaster university', 'university of bristol', 'university of st andrews', 'university of bath', 'university of surrey', 'university of kent', 'queen\'s university belfast'
        'university of east anglia', 'cardiff university', 'university of aberdeen', 'university of strathclyde', 'loughborough university', 'university of reading', 'heriot-watt university', 'university of dundee', 'city, university of london', 'university of the arts london'
        'university of essex', 'university of the west of england', 'royal holloway, university of london', 'sheffield hallam university', 'brunel university london', 'university of portsmouth', 'coventry university', 'university of plymouth', 'manchester metropolitan university', 'nottingham trent university'
    ]
}
INSTITUTE_NAMES['en_loose'] = INSTITUTE_NAMES['en']

LAST_NAMES = {
    'zh': [
        # https://www.sinosplice.com/learn-chinese/chinese-vocabulary-lists/the-top-100-chinese-surnames
        'li', 'wang', 'zhang', 'liu', 'chen', 'yang', 'zhao', 'huang', 'zhou', 'wu',
        'xu', 'sun', 'hu', 'zhu', 'gao', 'lin', 'he', 'guo', 'ma', 'luo',
        'liang', 'song', 'zheng', 'xie', 'han', 'tang', 'feng', 'yu', 'dong', 'xiao',
        'cheng', 'cao', 'yuan', 'deng', 'xu', 'fu', 'shen', 'zeng', 'peng', 'lu',
        'su', 'lu', 'jiang', 'cai', 'jia', 'ding', 'wei', 'xue', 'ye', 'yan',
        'yu', 'pan', 'du', 'dai', 'xia', 'zhong', 'wang', 'tian', 'ren', 'jiang',
        'fan', 'fang', 'shi', 'yao', 'tan', 'sheng', 'zou', 'xiong', 'jin', 'lu',
        'hao', 'kong', 'bai', 'cui', 'kang', 'mao', 'qiu', 'qin', 'jiang', 'shi',
        'gu', 'hou', 'shao', 'meng', 'long', 'wan', 'duan', 'zhang', 'qian', 'tang',
        'yin', 'li', 'yi', 'chang', 'wu', 'qiao', 'he', 'lai', 'gong', 'wen',
        # More: https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames
        'tan, ''liao', 'xiong', 'lei', 'tao', 'wan', 'mo',
    ],
    'en': [
        # https://names.mongabay.com/data/1000.html
        'smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', 'davis', 'rodriguez', 'martinez'
        'hernandez', 'lopez', 'gonzalez', 'wilson', 'anderson', 'thomas', 'taylor', 'moore', 'jackson', 'martin'
        'lee', 'perez', 'thompson', 'white', 'harris', 'sanchez', 'clark', 'ramirez', 'lewis', 'robinson'
        'walker', 'young', 'allen', 'king', 'wright', 'scott', 'torres', 'nguyen', 'hill', 'flores'
        'green', 'adams', 'nelson', 'baker', 'hall', 'rivera', 'campbell', 'mitchell', 'carter', 'roberts'
        'gomez', 'phillips', 'evans', 'turner', 'diaz', 'parker', 'cruz', 'edwards', 'collins', 'reyes'
        'stewart', 'morris', 'morales', 'murphy', 'cook', 'rogers', 'gutierrez', 'ortiz', 'morgan', 'cooper'
        'peterson', 'bailey', 'reed', 'kelly', 'howard', 'ramos', 'kim', 'cox', 'ward', 'richardson'
        'watson', 'brooks', 'chavez', 'wood', 'james', 'bennett', 'gray', 'mendoza', 'ruiz', 'hughes'
        'price', 'alvarez', 'castillo', 'sanders', 'patel', 'myers', 'ross', 'foster', 'jimenez', 'powell'
        'jenkins', 'perry', 'russell', 'sullivan', 'bell', 'coleman', 'butler', 'henderson', 'barnes', 'gonzales'
        'fisher', 'vasquez', 'simmons', 'romero', 'jordan', 'patterson', 'alexander', 'hamilton', 'graham', 'reynolds'
        'griffin', 'wallace', 'moreno', 'west', 'cole', 'hayes', 'bryant', 'herrera', 'gibson', 'ellis'
        'tran', 'medina', 'aguilar', 'stevens', 'murray', 'ford', 'castro', 'marshall', 'owens', 'harrison'
        'fernandez', 'mcdonald', 'woods', 'washington', 'kennedy', 'wells', 'vargas', 'henry', 'freeman', 'webb'
        'tucker', 'guzman', 'burns', 'crawford', 'olson', 'simpson', 'porter', 'hunter', 'gordon', 'mendez'
        'silva', 'shaw', 'snyder', 'mason', 'dixon', 'munoz', 'hunt', 'hicks', 'holmes', 'palmer'
        'wagner', 'black', 'robertson', 'boyd', 'rose', 'stone', 'salazar', 'fox', 'warren', 'mills'
        'meyer', 'rice', 'schmidt', 'garza', 'daniels', 'ferguson', 'nichols', 'stephens', 'soto', 'weaver'
        'ryan', 'gardner', 'payne', 'grant', 'dunn', 'kelley', 'spencer', 'hawkins', 'arnold', 'pierce'
        'vazquez', 'hansen', 'peters', 'santos', 'hart', 'bradley', 'knight', 'elliott', 'cunningham', 'duncan'
        'armstrong', 'hudson', 'carroll', 'lane', 'riley', 'andrews', 'alvarado', 'ray', 'delgado', 'berry'
        'perkins', 'hoffman', 'johnston', 'matthews', 'pena', 'richards', 'contreras', 'willis', 'carpenter', 'lawrence'
        'sandoval', 'guerrero', 'george', 'chapman', 'rios', 'estrada', 'ortega', 'watkins', 'greene', 'nunez'
        'wheeler', 'valdez', 'harper', 'burke', 'larson', 'santiago', 'maldonado', 'morrison', 'franklin', 'carlson'
        'austin', 'dominguez', 'carr', 'lawson', 'jacobs', 'obrien', 'lynch', 'singh', 'vega', 'bishop'
        'montgomery', 'oliver', 'jensen', 'harvey', 'williamson', 'gilbert', 'dean', 'sims', 'espinoza', 'howell'
        'wong', 'reid', 'hanson', 'le', 'mccoy', 'garrett', 'burton', 'fuller', 'weber', 'welch'
        'rojas', 'lucas', 'marquez', 'fields', 'park', 'little', 'banks', 'padilla', 'day', 'walsh'
        'bowman', 'schultz', 'luna', 'fowler', 'mejia', 'davidson', 'acosta', 'brewer', 'may', 'holland'
        'juarez', 'newman', 'pearson', 'curtis', 'cortez', 'douglas', 'schneider', 'joseph', 'barrett', 'navarro'
        'figueroa', 'keller', 'avila', 'wade', 'molina', 'stanley', 'hopkins', 'campos', 'barnett', 'bates'
        'chambers', 'caldwell', 'beck', 'lambert', 'miranda', 'byrd', 'craig', 'ayala', 'lowe', 'frazier'
        'powers', 'neal', 'leonard', 'gregory', 'carrillo', 'sutton', 'fleming', 'rhodes', 'shelton', 'schwartz'
        'norris', 'jennings', 'watts', 'duran', 'walters', 'cohen', 'mcdaniel', 'moran', 'parks', 'steele'
        'vaughn', 'becker', 'holt', 'deleon', 'barker', 'terry', 'hale', 'leon', 'hail', 'benson'
        'haynes', 'horton', 'miles', 'lyons', 'pham', 'graves', 'bush', 'thornton', 'wolfe', 'warner'
        'cabrera', 'mckinney', 'mann', 'zimmerman', 'dawson', 'lara', 'fletcher', 'page', 'mccarthy', 'love'
        'robles', 'cervantes', 'solis', 'erickson', 'reeves', 'klein', 'salinas', 'fuentes', 'baldwin', 'daniel'
        'simon', 'velasquez', 'hardy', 'higgins', 'aguirre', 'cummings', 'chandler', 'sharp', 'barber', 'bowen'
        'ochoa', 'dennis', 'robbins', 'ramsey', 'francis', 'griffith', 'paul', 'blair', 'oconnor', 'cardenas'
        'pacheco', 'cross', 'calderon', 'quinn', 'moss', 'swanson', 'chan', 'rivas', 'khan', 'rodgers'
        'serrano', 'fitzgerald', 'rosales', 'stevenson', 'christensen', 'manning', 'gill', 'curry', 'mclaughlin', 'harmon'
        'mcgee', 'gross', 'doyle', 'garner', 'newton', 'burgess', 'reese', 'walton', 'blake', 'trujillo'
        'adkins', 'brady', 'goodman', 'roman', 'webster', 'goodwin', 'fischer', 'potter', 'delacruz', 'montoya'
        'todd', 'hines', 'mullins', 'castaneda', 'malone', 'cannon', 'tate', 'mack', 'sherman', 'hubbard'
        'hodges', 'guerra', 'wolf', 'valencia', 'franco', 'saunders', 'rowe', 'gallagher', 'farmer', 'hammond'
        'hampton', 'townsend', 'ingram', 'wise', 'gallegos', 'clarke', 'barton', 'schroeder', 'maxwell', 'waters'
        'logan', 'camacho', 'strickland', 'norman', 'person', 'colon', 'parsons', 'frank', 'harrington', 'glover'
        'osborne', 'buchanan', 'casey', 'floyd', 'patton', 'ibarra', 'ball', 'tyler', 'suarez', 'bowers'
        'orozco', 'salas', 'cobb', 'gibbs', 'andrade', 'bauer', 'conner', 'moody', 'escobar', 'mcguire'
        'lloyd', 'mueller', 'hartman', 'french', 'kramer', 'mcbride', 'pope', 'lindsey', 'velazquez', 'norton'
        'mccormick', 'sparks', 'flynn', 'yates', 'hogan', 'marsh', 'macias', 'villanueva', 'zamora', 'pratt'
        'stokes', 'owen', 'ballard', 'lang', 'brock', 'villarreal', 'charles', 'drake', 'barrera', 'cain'
        'patrick', 'pineda', 'burnett', 'mercado', 'santana', 'shepherd', 'bautista', 'ali', 'shaffer', 'lamb'
        'trevino', 'mckenzie', 'hess', 'beil', 'olsen', 'cochran', 'morton', 'nash', 'wilkins', 'petersen'
        'briggs', 'shah', 'roth', 'nicholson', 'holloway', 'lozano', 'flowers', 'rangel', 'hoover', 'arias'
        'short', 'mora', 'valenzuela', 'bryan', 'meyers', 'weiss', 'underwood', 'bass', 'greer', 'summers'
        'houston', 'carson', 'morrow', 'clayton', 'whitaker', 'decker', 'yoder', 'collier', 'zuniga', 'carey'
        'wilcox', 'melendez', 'poole', 'roberson', 'larsen', 'conley', 'davenport', 'copeland', 'massey', 'lam'
        'huff', 'rocha', 'cameron', 'jefferson', 'hood', 'monroe', 'anthony', 'pittman', 'huynh', 'randall'
        'singleton', 'kirk', 'combs', 'mathis', 'christian', 'skinner', 'bradford', 'richard', 'galvan', 'wall'
        'boone', 'kirby', 'wilkinson', 'bridges', 'bruce', 'atkinson', 'velez', 'meza', 'roy', 'vincent'
        'york', 'hodge', 'villa', 'abbott', 'allison', 'tapia', 'gates', 'chase', 'sosa', 'sweeney'
        'farrell', 'wyatt', 'dalton', 'horn', 'barron', 'phelps', 'dickerson', 'heath', 'foley', 'atkins'
        'mathews', 'bonilla', 'acevedo', 'benitez', 'zavala', 'hensley', 'glenn', 'cisneros', 'harrell', 'shields'
        'rubio', 'choi', 'huffman', 'boyer', 'garrison', 'arroyo', 'bond', 'kane', 'hancock', 'callahan'
        'dillon', 'cline', 'wiggins', 'grimes', 'arellano', 'melton', 'oneill', 'savage', 'ho', 'beltran'
        'pitts', 'parrish', 'ponce', 'rich', 'booth', 'koch', 'golden', 'ware', 'brennan', 'mcdowell'
        'marks', 'cantu', 'humphrey', 'baxter', 'sawyer', 'clay', 'tanner', 'hutchinson', 'kaur', 'berg'
        'wiley', 'gilmore', 'russo', 'villegas', 'hobbs', 'keith', 'wilkerson', 'ahmed', 'beard', 'mcclain'
        'montes', 'mata', 'rosario', 'vang', 'walter', 'henson', 'oneal', 'mosley', 'mcclure', 'beasley'
        'stephenson', 'snow', 'huerta', 'preston', 'vance', 'barry', 'johns', 'eaton', 'blackwell', 'dyer'
        'prince', 'macdonald', 'solomon', 'guevara', 'stafford', 'english', 'hurst', 'woodard', 'cortes', 'shannon'
        'kemp', 'nolan', 'mccullough', 'merritt', 'murillo', 'moon', 'salgado', 'strong', 'kline', 'cordova'
        'barajas', 'roach', 'rosas', 'winters', 'jacobson', 'lester', 'knox', 'bullock', 'kerr', 'leach'
        'meadows', 'davila', 'orr', 'whitehead', 'pruitt', 'kent', 'conway', 'mckee', 'barr', 'david'
        'dejesus', 'marin', 'berger', 'mcintyre', 'blankenship', 'gaines', 'palacios', 'cuevas', 'bartlett', 'durham'
        'dorsey', 'mccall', 'odonnell', 'stein', 'browning', 'stout', 'lowery', 'sloan', 'mclean', 'hendricks'
        'calhoun', 'sexton', 'chung', 'gentry', 'hull', 'duarte', 'ellison', 'nielsen', 'gillespie', 'buck'
        'middleton', 'sellers', 'leblanc', 'esparza', 'hardin', 'bradshaw', 'mcintosh', 'howe', 'livingston', 'frost'
        'glass', 'morse', 'knapp', 'herman', 'stark', 'bravo', 'noble', 'spears', 'weeks', 'corona'
        'frederick', 'buckley', 'mcfarland', 'hebert', 'enriquez', 'hickman', 'quintero', 'randolph', 'schaefer', 'walls'
        'trejo', 'house', 'reilly', 'pennington', 'michael', 'conrad', 'giles', 'benjamin', 'crosby', 'fitzpatrick'
        'donovan', 'mays', 'mahoney', 'valentine', 'raymond', 'medrano', 'hahn', 'mcmillan', 'small', 'bentley'
        'felix', 'peck', 'lucero', 'boyle', 'hanna', 'pace', 'rush', 'hurley', 'harding', 'mcconnell'
        'bernal', 'nava', 'ayers', 'everett', 'ventura', 'avery', 'pugh', 'mayer', 'bender', 'shepard'
        'mcmahon', 'landry', 'case', 'sampson', 'moses', 'magana', 'blackburn', 'dunlap', 'gould', 'duffy'
        'vaughan', 'herring', 'mckay', 'espinosa', 'rivers', 'farley', 'bernard', 'ashley', 'friedman', 'potts'
        'truong', 'costa', 'correa', 'blevins', 'nixon', 'clements', 'fry', 'delarosa', 'best', 'benton'
        'lugo', 'portillo', 'dougherty', 'crane', 'haley', 'phan', 'villalobos', 'blanchard', 'horne', 'finley'
        'quintana', 'lynn', 'esquivel', 'bean', 'dodson', 'mullen', 'hayden', 'cano', 'levy', 'huber'
        'richmond', 'moyer', 'lim', 'frye', 'sheppard', 'mccarty', 'avalos', 'booker', 'waller', 'parra'
        'woodward', 'jaramillo', 'krueger', 'rasmussen', 'brandt', 'peralta', 'donaldson', 'stuart', 'faulkner', 'maynard'
        'galindo', 'coffey', 'estes', 'sanford', 'burch', 'maddox', 'vo', 'oconnell', 'vu', 'andersen'
        'spence', 'mcpherson', 'church', 'schmitt', 'stanton', 'leal', 'cherry', 'compton', 'dudley', 'sierra'
        'pollard', 'alfaro', 'hester', 'proctor', 'hinton', 'novak', 'good', 'madden', 'mccann', 'terrell'
        'jarvis', 'dickson', 'reyna', 'cantrell', 'mayo', 'branch', 'hendrix', 'rollins', 'rowland', 'whitney'
        'duke', 'odom', 'daugherty', 'travis'
    ]
}
LAST_NAMES['en_loose'] = LAST_NAMES['en']

QUERIES = {
    'zh': [
        # cs
        '计算机理论', '信息 编码理论', '算法 数据结构', '程序语言理论', '形式方法', '计算机系统', '计算机体系结构 计算机工程', '操作系统', '并发 平行 分布系统', '计算机网络'
        '计算机安全 密码学', '数据库', '计算机应用技术', '计算机图形学', '科学计算', '多媒体技术', '数据挖掘', '人工智能', '自动推理', '机器学习'
        '计算机视觉', '自然语言处理', '软件工程',
        # econ
        '微观经济学', '经济 发展', '市场', '生产 成本 效率', '专精', '供给 需求', '公司', '不确定性 博弈论', '市场失灵', '公共产业'
        '宏观经济学', '成长', '景气循环', '失业', '通货膨胀 货币政策', '财政政策',
        # eess
        '电气工程学', '电力电子学', '控制工程', '电子工程', '微电子学', '信号处理', '通信工程', '测量', '计算机工程',
        # math
        '基础 哲学', '纯粹数学', '数量', '结构', '空间', '变化', '离散数学', '应用数学',
        # physics
        '粒子物理学', '标准模型', '量子场论', '量子电动力学', '量子色动力学', '电弱理论', '晶格场论', '晶格规范理论', '规范场论', '超对称'
        '大统一理论', '超弦理论', 'm理论', '原子分子 光物理学', '量子光学', '量子化学', '量子信息学', '凝聚态物理学', 'bcs理论', '布洛赫波'
        '密度泛函理论', '费米气体', '费米液体', '统计力学', '天文物理学', '大爆炸', '宇宙暴胀', '广义相对论', '牛顿万有引力定律', '磁流体力学',
        # q-bio
        '生物分子', '基因组学', '分子网络', '神经元 认知', '人口 进化', '定量方法', '亚细胞过程', '组织和器官',
        # q-fin
        '计量金融', '金融数学', '项目组合管理', '证券定价', '风险管理', '金融统计', '市场微结构模型',
        # stat
        '概率论 数理统计', '抽样 抽样分布', '统计数据 搜集 整理 显示', '参数估计', '非参数估计', '假设检验', '方差分析', '非参数统计', '时间序列分析', '统计指数'
        '多变量分析', '主成分分析 因子分析', '聚类分析 判别分析', '结构方程式模式', '相关分析 回归分析'
    ]
}

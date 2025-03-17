import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve

text = """
Designated Priority: 1
Q-values before update: [[0.97250193 1.0073968 ]]
Q-values after update: [[0.96799123 1.0049738 ]]
Designated Priority: 1
Q-values before update: [[0.9691602 1.0054127]]
Q-values after update: [[0.96523094 1.0041952 ]]
Designated Priority: 1
Q-values before update: [[0.96577173 1.0030856 ]]
Q-values after update: [[0.96253884 1.0034198 ]]
Designated Priority: 1
Q-values before update: [[0.960212   0.99134994]]
Q-values after update: [[0.9583245 0.9948544]]
Designated Priority: 1
Q-values before update: [[0.9557541 0.9807562]]
Q-values after update: [[0.95605195 0.98922324]]
Designated Priority: 3
Q-values before update: [[0.95178664 0.9737259 ]]
Q-values after update: [[0.95828927 0.99439377]]
Episode 77 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [ 0.14976732  1.9589839  -0.22854702 -2.9980547 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[0.9624324 1.0257033]]
Q-values after update: [[0.9630438 1.0326585]]
Designated Priority: 1
Q-values before update: [[0.9628446 1.0340639]]
Q-values after update: [[0.963532 1.040354]]
Designated Priority: 1
Q-values before update: [[0.9633631 1.0419933]]
Q-values after update: [[0.9640907 1.0476311]]
Designated Priority: 1
Q-values before update: [[0.96456933 1.050265  ]]
Q-values after update: [[0.9652178 1.0550258]]
Designated Priority: 1
Q-values before update: [[0.96628284 1.0586989 ]]
Q-values after update: [[0.9667256 1.0623838]]
Designated Priority: 1
Q-values before update: [[0.96939975 1.0671761 ]]
Q-values after update: [[0.9722526 1.0719359]]
Designated Priority: 1
Q-values before update: [[0.97287905 1.0726004 ]]
Q-values after update: [[0.9746643 1.0749121]]
Designated Priority: 1
Q-values before update: [[0.9783229 1.0810426]]
Q-values after update: [[0.97938097 1.0814705 ]]
Designated Priority: 3
Q-values before update: [[0.9821793 1.0866625]]
Q-values after update: [[0.987618  1.0897284]]
Episode 78 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [ 0.09185012  0.9648694  -0.22146733 -1.7427465 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[0.969305 1.050322]]
Q-values after update: [[0.97321415 1.0511913 ]]
Designated Priority: 1
Q-values before update: [[0.9708047 1.0468686]]
Q-values after update: [[0.97369814 1.0459119 ]]
Designated Priority: 1
Q-values before update: [[0.9759513 1.0500946]]
Q-values after update: [[0.97833645 1.0479896 ]]
Designated Priority: 1
Q-values before update: [[0.98131   1.0529745]]
Q-values after update: [[0.98321795 1.0498726 ]]
Designated Priority: 1
Q-values before update: [[0.9863627 1.0555298]]
Q-values after update: [[0.9888505 1.0531092]]
Designated Priority: 1
Q-values before update: [[0.9872328 1.0493327]]
Q-values after update: [[0.98889923 1.045711  ]]
Designated Priority: 1
Q-values before update: [[0.99208486 1.0515816 ]]
Q-values after update: [[0.99336153 1.0472178 ]]
Designated Priority: 1
Q-values before update: [[0.99665534 1.0532998 ]]
Q-values after update: [[0.9975202 1.0483228]]
Designated Priority: 1
Q-values before update: [[1.0013113 1.0550355]]
Q-values after update: [[1.0017754 1.0495572]]
Designated Priority: 1
Q-values before update: [[1.0064241 1.0568844]]
Q-values after update: [[1.0065017 1.0510168]]
Designated Priority: 1
Q-values before update: [[1.0127366 1.0591431]]
Q-values after update: [[1.0124723 1.0530121]]
Designated Priority: 1
Q-values before update: [[1.018243  1.0605266]]
Q-values after update: [[1.0177685 1.0543975]]
Designated Priority: 3
Q-values before update: [[1.021948  1.0598404]]
Q-values after update: [[1.0112263 1.0326746]]
Episode 79 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.14000055  1.8035268  -0.24868774 -2.8854253 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[0.983875   0.99520206]]
Q-values after update: [[0.980888  0.9823252]]
Designated Priority: 1
Q-values before update: [[0.98291945 0.9855211 ]]
Q-values after update: [[0.9799073  0.97399044]]
Designated Priority: 1
Q-values before update: [[0.98185277 0.9767333 ]]
Q-values after update: [[0.9792572  0.96592116]]
Designated Priority: 1
Q-values before update: [[0.97917676 0.965546  ]]
Q-values after update: [[0.9777889 0.9566871]]
Designated Priority: 1
Q-values before update: [[0.9774945 0.9561347]]
Q-values after update: [[0.977502  0.9490031]]
Designated Priority: 1
Q-values before update: [[0.97705626 0.94848025]]
Q-values after update: [[0.9778091 0.9439574]]
Designated Priority: 1
Q-values before update: [[0.97720647 0.94375813]]
Q-values after update: [[0.9785373 0.9396113]]
Designated Priority: 1
Q-values before update: [[0.97873753 0.93994856]]
Q-values after update: [[0.9814743 0.9369947]]
Designated Priority: 1
Q-values before update: [[0.9814676 0.9372586]]
Q-values after update: [[0.9857534  0.93545425]]
Designated Priority: 1
Q-values before update: [[0.9855654  0.93564343]]
Q-values after update: [[0.99151284 0.9349735 ]]
Designated Priority: 1
Q-values before update: [[0.98888195 0.9405435 ]]
Q-values after update: [[0.99667025 0.9409953 ]]
Designated Priority: 1
Q-values before update: [[0.9939953  0.95099443]]
Q-values after update: [[1.0040765  0.95270467]]
Designated Priority: 1
Q-values before update: [[1.0010878  0.96445554]]
Q-values after update: [[1.0138509 0.9676398]]
Designated Priority: 1
Q-values before update: [[1.0110582 0.9797791]]
Q-values after update: [[1.0269222  0.98467886]]
Designated Priority: 1
Q-values before update: [[1.0258629 0.9982443]]
Q-values after update: [[1.0444449 1.0046086]]
Designated Priority: 1
Q-values before update: [[1.0432335 1.0196848]]
Q-values after update: [[1.0634353 1.0311644]]
Designated Priority: 3
Q-values before update: [[1.0575012 1.0140667]]
Q-values after update: [[1.0733273 1.0199996]]
Episode 80 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [-0.2214799  -1.3241235   0.22618586  2.0302384 ], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[1.0549898 0.9363854]]
Q-values after update: [[1.062877   0.93761635]]
Designated Priority: 1
Q-values before update: [[1.0692937  0.94328034]]
Q-values after update: [[1.0756302 0.9443768]]
Designated Priority: 1
Q-values before update: [[1.0818486 0.950027 ]]
Q-values after update: [[1.086574  0.9508835]]
Designated Priority: 1
Q-values before update: [[1.0928389  0.95787084]]
Q-values after update: [[1.09608    0.95839614]]
Designated Priority: 1
Q-values before update: [[1.1015749 0.9742   ]]
Q-values after update: [[1.1031952  0.97427976]]
Designated Priority: 1
Q-values before update: [[1.1079638 0.9921841]]
Q-values after update: [[1.1079566  0.99174476]]
Designated Priority: 1
Q-values before update: [[1.1125371 1.0097616]]
Q-values after update: [[1.1136446 1.0116919]]
Designated Priority: 1
Q-values before update: [[1.1045507  0.99259675]]
Q-values after update: [[1.1038549 0.9934995]]
Designated Priority: 3
Q-values before update: [[1.1092103 1.0127618]]
Q-values after update: [[1.0840783 1.0026649]]
Episode 81 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.10963928 -1.418997    0.21773586  2.232652  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0554038 0.9307852]]
Q-values after update: [[1.0394857 0.9257529]]
Designated Priority: 1
Q-values before update: [[1.0455394 0.931695 ]]
Q-values after update: [[1.0311456  0.92854416]]
Designated Priority: 1
Q-values before update: [[1.0258436  0.92300427]]
Q-values after update: [[1.0133438 0.9205215]]
Designated Priority: 1
Q-values before update: [[1.0177662 0.925371 ]]
Q-values after update: [[1.0059813  0.92269075]]
Designated Priority: 1
Q-values before update: [[1.0091827 0.9266288]]
Q-values after update: [[0.9986216 0.9239937]]
Designated Priority: 1
Q-values before update: [[1.0007199  0.92707884]]
Q-values after update: [[0.99186915 0.92473936]]
Designated Priority: 1
Q-values before update: [[0.98992395 0.9381974 ]]
Q-values after update: [[0.9830743  0.93650115]]
Designated Priority: 1
Q-values before update: [[0.98039293 0.9500607 ]]
Q-values after update: [[0.97647685 0.9493394 ]]
Designated Priority: 1
Q-values before update: [[0.97441244 0.9637142 ]]
Q-values after update: [[0.9742269 0.9644282]]
Designated Priority: 1
Q-values before update: [[0.97454387 0.98095477]]
Q-values after update: [[0.97591907 0.98561746]]
Designated Priority: 3
Q-values before update: [[0.97346294 0.96986246]]
Q-values after update: [[0.97937536 0.975932  ]]
Episode 82 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.14744096 -1.3336912   0.22735462  2.2340846 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[0.98330724 0.92373943]]
Q-values after update: [[0.98741555 0.92731225]]
Designated Priority: 1
Q-values before update: [[0.9899597  0.93121755]]
Q-values after update: [[0.99476326 0.93498397]]
Designated Priority: 1
Q-values before update: [[0.9969691  0.93865883]]
Q-values after update: [[1.0025277 0.9426429]]
Designated Priority: 1
Q-values before update: [[1.0044279 0.9461012]]
Q-values after update: [[1.0104972 0.9523386]]
Designated Priority: 1
Q-values before update: [[1.0058105 0.9464123]]
Q-values after update: [[1.0118989  0.95209813]]
Designated Priority: 1
Q-values before update: [[1.0144553  0.95621395]]
Q-values after update: [[1.0211277  0.96197003]]
Designated Priority: 1
Q-values before update: [[1.0207477  0.97759545]]
Q-values after update: [[1.0278158 0.9853401]]
Designated Priority: 1
Q-values before update: [[1.0242441 0.9675658]]
Q-values after update: [[1.031093   0.97646666]]
Designated Priority: 1
Q-values before update: [[1.026225   0.96818984]]
Q-values after update: [[1.0326493  0.97594553]]
Designated Priority: 1
Q-values before update: [[1.0358751 0.9854998]]
Q-values after update: [[1.0424235  0.99322647]]
Designated Priority: 1
Q-values before update: [[1.0440483 1.0121572]]
Q-values after update: [[1.0509076 1.0198088]]
Designated Priority: 1
Q-values before update: [[1.0537218 1.0398917]]
Q-values after update: [[1.0608761 1.0474594]]
Designated Priority: 3
Q-values before update: [[1.0681491 1.0709674]]
Q-values after update: [[1.0676577 1.0599624]]
Episode 83 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.17601335 -0.94291914  0.2270463   1.7082077 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0552208  0.98688334]]
Q-values after update: [[1.0555142  0.98115563]]
Designated Priority: 1
Q-values before update: [[1.0601271  0.98719037]]
Q-values after update: [[1.0603054 0.982088 ]]
Designated Priority: 1
Q-values before update: [[1.0547311  0.97550625]]
Q-values after update: [[1.0538144 0.9708156]]
Designated Priority: 1
Q-values before update: [[1.0581142 0.9762565]]
Q-values after update: [[1.0560288 0.9713849]]
Designated Priority: 1
Q-values before update: [[1.0595702 0.9760541]]
Q-values after update: [[1.0566812 0.9711182]]
Designated Priority: 1
Q-values before update: [[1.0595001 0.9750513]]
Q-values after update: [[1.0561997 0.9701752]]
Designated Priority: 1
Q-values before update: [[1.0559872 0.9810115]]
Q-values after update: [[1.05282   0.9760965]]
Designated Priority: 1
Q-values before update: [[1.052158  0.9898896]]
Q-values after update: [[1.0499289 0.9871706]]
Designated Priority: 1
Q-values before update: [[1.0454801  0.96989536]]
Q-values after update: [[1.0438466 0.9677104]]
Designated Priority: 1
Q-values before update: [[1.0431166  0.98156464]]
Q-values after update: [[1.0423483 0.9797646]]
Designated Priority: 1
Q-values before update: [[1.0411664  0.99341124]]
Q-values after update: [[1.0415651  0.99441457]]
Designated Priority: 1
Q-values before update: [[1.0368793  0.97788405]]
Q-values after update: [[1.0383263  0.97921634]]
Designated Priority: 1
Q-values before update: [[1.0407524  0.99551463]]
Q-values after update: [[1.0436106 0.9974114]]
Designated Priority: 3
Q-values before update: [[1.0439465 1.0137762]]
Q-values after update: [[1.0364647 1.0107062]]
Episode 84 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [-0.15686658 -1.5615551   0.25028968  2.527814  ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[1.0364741 0.9491911]]
Q-values after update: [[1.0319346 0.9481957]]
Designated Priority: 1
Q-values before update: [[1.0352678 0.9522166]]
Q-values after update: [[1.0314021  0.95246565]]
Designated Priority: 1
Q-values before update: [[1.0276182  0.94802445]]
Q-values after update: [[1.0237362 0.9481832]]
Designated Priority: 1
Q-values before update: [[1.0267041 0.9519156]]
Q-values after update: [[1.0234783 0.9532677]]
Designated Priority: 1
Q-values before update: [[1.0200783 0.9490932]]
Q-values after update: [[1.0178494 0.9520687]]
Designated Priority: 1
Q-values before update: [[1.0151266 0.9482819]]
Q-values after update: [[1.012821  0.9509006]]
Designated Priority: 1
Q-values before update: [[1.0160918 0.9551777]]
Q-values after update: [[1.0143762  0.95896506]]
Designated Priority: 1
Q-values before update: [[1.0118439 0.9552816]]
Q-values after update: [[1.0100496 0.9586391]]
Designated Priority: 1
Q-values before update: [[1.0130833  0.96280104]]
Q-values after update: [[1.0111511  0.96570265]]
Designated Priority: 1
Q-values before update: [[1.0133468  0.96891034]]
Q-values after update: [[1.0115614 0.9714867]]
Designated Priority: 1
Q-values before update: [[1.0130672  0.97405857]]
Q-values after update: [[1.0117297  0.97645354]]
Designated Priority: 1
Q-values before update: [[1.0125878 0.9784045]]
Q-values after update: [[1.0117314 0.981699 ]]
Designated Priority: 1
Q-values before update: [[1.0078768  0.97677183]]
Q-values after update: [[1.007626  0.9799121]]
Designated Priority: 1
Q-values before update: [[1.0085427  0.98193496]]
Q-values after update: [[1.009115  0.9850818]]
Designated Priority: 1
Q-values before update: [[1.0054439 0.9965464]]
Q-values after update: [[1.0072039 0.9999   ]]
Designated Priority: 1
Q-values before update: [[1.0041102 1.01245  ]]
Q-values after update: [[1.007628  1.0163286]]
Designated Priority: 1
Q-values before update: [[1.0040885 1.0286596]]
Q-values after update: [[1.0078018 1.0333102]]
Designated Priority: 1
Q-values before update: [[1.0046326 1.0168188]]
Q-values after update: [[1.008266  1.0220058]]
Designated Priority: 3
Q-values before update: [[1.0059875 1.0069644]]
Q-values after update: [[1.0086185 1.0100998]]
Episode 85 out of total 100, Total Reward: 19.0, Epsilon: 0.75, Current State: [-0.10195947 -0.5917548   0.21584615  1.1275084 ], Steps Taken: 19
Designated Priority: 1
Q-values before update: [[1.0207976  0.99843085]]
Q-values after update: [[1.0223172 1.0007043]]
Designated Priority: 1
Q-values before update: [[1.0250866 1.0046799]]
Q-values after update: [[1.0262953 1.0067394]]
Designated Priority: 1
Q-values before update: [[1.0285298 1.0101961]]
Q-values after update: [[1.0296555 1.0121238]]
Designated Priority: 1
Q-values before update: [[1.031376  1.0150665]]
Q-values after update: [[1.0326657 1.0169601]]
Designated Priority: 1
Q-values before update: [[1.0309768 1.0259869]]
Q-values after update: [[1.0328209 1.0280031]]
Designated Priority: 1
Q-values before update: [[1.030598  1.0411183]]
Q-values after update: [[1.0323317 1.0429614]]
Designated Priority: 1
Q-values before update: [[1.0288768 1.0253348]]
Q-values after update: [[1.0310438 1.0271931]]
Designated Priority: 1
Q-values before update: [[1.0290604 1.0407764]]
Q-values after update: [[1.0322757 1.0430424]]
Designated Priority: 1
Q-values before update: [[1.0301454 1.0567809]]
Q-values after update: [[1.0331466 1.0588263]]
Designated Priority: 1
Q-values before update: [[1.0288742 1.0413107]]
Q-values after update: [[1.0315484 1.0433109]]
Designated Priority: 1
Q-values before update: [[1.0281457 1.0271449]]
Q-values after update: [[1.0306699 1.0294847]]
Designated Priority: 3
Q-values before update: [[1.0279206 1.0141776]]
Q-values after update: [[1.0256504 1.0143242]]
Episode 86 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.12773645 -0.76014555  0.2283453   1.392305  ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.0303291 1.0116124]]
Q-values after update: [[1.0280669 1.0116826]]
Designated Priority: 1
Q-values before update: [[1.0321062 1.0168171]]
Q-values after update: [[1.0297523 1.016768 ]]
Designated Priority: 1
Q-values before update: [[1.0330791 1.0212152]]
Q-values after update: [[1.0309    1.0211475]]
Designated Priority: 1
Q-values before update: [[1.0335462 1.0249212]]
Q-values after update: [[1.0318346 1.0249575]]
Designated Priority: 1
Q-values before update: [[1.0301137 1.0381757]]
Q-values after update: [[1.0284797 1.0381142]]
Designated Priority: 1
Q-values before update: [[1.0257411 1.0213356]]
Q-values after update: [[1.0248855 1.0214982]]
Designated Priority: 1
Q-values before update: [[1.0232235 1.0359608]]
Q-values after update: [[1.0224531 1.0361776]]
Designated Priority: 1
Q-values before update: [[1.0192785 1.0195891]]
Q-values after update: [[1.0187578 1.0203022]]
Designated Priority: 1
Q-values before update: [[1.0150212 1.0112345]]
Q-values after update: [[1.015306  1.0121223]]
Designated Priority: 1
Q-values before update: [[1.0166357 1.0217676]]
Q-values after update: [[1.0171064 1.0232432]]
Designated Priority: 3
Q-values before update: [[1.0138364 1.0124041]]
Q-values after update: [[1.0121582 1.0127919]]
Episode 87 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.12949726 -0.58807415  0.21547772  1.2201648 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.021369  1.0177014]]
Q-values after update: [[1.0199103 1.0178667]]
Designated Priority: 1
Q-values before update: [[1.016159  1.0126079]]
Q-values after update: [[1.0143675 1.0125701]]
Designated Priority: 1
Q-values before update: [[1.01896   1.0185806]]
Q-values after update: [[1.0172454 1.0182514]]
Designated Priority: 1
Q-values before update: [[1.013459  1.0129353]]
Q-values after update: [[1.011486  1.0124705]]
Designated Priority: 1
Q-values before update: [[1.016016  1.0184546]]
Q-values after update: [[1.0141369 1.0177228]]
Designated Priority: 1
Q-values before update: [[1.0103116 1.0123396]]
Q-values after update: [[1.008261  1.0115392]]
Designated Priority: 1
Q-values before update: [[1.0127468 1.0175201]]
Q-values after update: [[1.0108049 1.0165   ]]
Designated Priority: 1
Q-values before update: [[1.006939  1.0110424]]
Q-values after update: [[1.0052443 1.010275 ]]
Designated Priority: 1
Q-values before update: [[1.0013745 1.0044808]]
Q-values after update: [[1.0000343 1.0043261]]
Designated Priority: 1
Q-values before update: [[0.99619776 0.9990376 ]]
Q-values after update: [[0.9953384 0.9998448]]
Designated Priority: 1
Q-values before update: [[0.99202955 0.99514604]]
Q-values after update: [[0.9918077 0.9972575]]
Designated Priority: 1
Q-values before update: [[0.9890155  0.99317527]]
Q-values after update: [[0.9896232 0.9969381]]
Designated Priority: 1
Q-values before update: [[0.9847317  0.98959804]]
Q-values after update: [[0.9865861 0.9958167]]
Designated Priority: 1
Q-values before update: [[0.98197067 0.98430026]]
Q-values after update: [[0.98562294 0.9939483 ]]
Designated Priority: 1
Q-values before update: [[0.98217154 0.9831491 ]]
Q-values after update: [[0.98826957 0.9973034 ]]
Designated Priority: 3
Q-values before update: [[0.9846957 0.9850346]]
Q-values after update: [[0.9940351 1.0051453]]
Episode 88 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [ 0.22636837  1.9784381  -0.25255057 -3.047901  ], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[1.010794  1.0495183]]
Q-values after update: [[1.0124269 1.0565991]]
Designated Priority: 1
Q-values before update: [[1.0106782 1.0540438]]
Q-values after update: [[1.0121715 1.0596808]]
Designated Priority: 1
Q-values before update: [[1.0108812 1.0577446]]
Q-values after update: [[1.0122459 1.0621396]]
Designated Priority: 1
Q-values before update: [[1.0116372 1.0612631]]
Q-values after update: [[1.012779  1.0644197]]
Designated Priority: 1
Q-values before update: [[1.0131214 1.0647745]]
Q-values after update: [[1.0139642 1.0667204]]
Designated Priority: 1
Q-values before update: [[1.015164  1.0682194]]
Q-values after update: [[1.0156285 1.0689651]]
Designated Priority: 1
Q-values before update: [[1.0180439 1.0715528]]
Q-values after update: [[1.0191828 1.0727781]]
Designated Priority: 1
Q-values before update: [[1.0230556 1.0781171]]
Q-values after update: [[1.0240154 1.079066 ]]
Designated Priority: 1
Q-values before update: [[1.0272864 1.0834517]]
Q-values after update: [[1.0271407 1.0818443]]
Designated Priority: 3
Q-values before update: [[1.0290208 1.0844257]]
Q-values after update: [[1.020295  1.0624822]]
Episode 89 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.13734737  1.1401083  -0.20947897 -1.9204355 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0100434 1.0482912]]
Q-values after update: [[1.00502   1.0322628]]
Designated Priority: 1
Q-values before update: [[1.0043181 1.0311437]]
Q-values after update: [[0.999215  1.0157561]]
Designated Priority: 1
Q-values before update: [[0.99813926 1.0138768 ]]
Q-values after update: [[0.99322903 0.9998466 ]]
Designated Priority: 1
Q-values before update: [[0.99190915 0.99800134]]
Q-values after update: [[0.9874755 0.9859688]]
Designated Priority: 1
Q-values before update: [[0.9863139 0.9842254]]
Q-values after update: [[0.98306775 0.9735253 ]]
Designated Priority: 1
Q-values before update: [[0.9881129 0.9795611]]
Q-values after update: [[0.9861195 0.9705231]]
Designated Priority: 1
Q-values before update: [[0.99051154 0.9760526 ]]
Q-values after update: [[0.98921   0.9682859]]
Designated Priority: 1
Q-values before update: [[0.9930013 0.9733459]]
Q-values after update: [[0.99226266 0.96666896]]
Designated Priority: 1
Q-values before update: [[0.9955097 0.9712993]]
Q-values after update: [[0.9955975  0.96569216]]
Designated Priority: 1
Q-values before update: [[0.99833345 0.97001004]]
Q-values after update: [[0.9989803 0.9652815]]
Designated Priority: 1
Q-values before update: [[1.0011739 0.9694189]]
Q-values after update: [[1.0025833  0.96557367]]
Designated Priority: 1
Q-values before update: [[1.0045407  0.96951306]]
Q-values after update: [[1.0070391 0.9665939]]
Designated Priority: 1
Q-values before update: [[1.0064613 0.9728672]]
Q-values after update: [[1.0102743  0.97089624]]
Designated Priority: 1
Q-values before update: [[1.0084379 0.98195  ]]
Q-values after update: [[1.0139736 0.9810515]]
Designated Priority: 1
Q-values before update: [[1.0122198 0.9925086]]
Q-values after update: [[1.0199139 0.9929916]]
Designated Priority: 1
Q-values before update: [[1.0174553 1.005333 ]]
Q-values after update: [[1.02781   1.0075011]]
Designated Priority: 1
Q-values before update: [[1.0252181 1.0196126]]
Q-values after update: [[1.0387781 1.0238777]]
Designated Priority: 1
Q-values before update: [[1.0339978 1.0353703]]
Q-values after update: [[1.0518614 1.0422947]]
Designated Priority: 1
Q-values before update: [[1.044557 1.053523]]
Q-values after update: [[1.0630519 1.0643214]]
Designated Priority: 1
Q-values before update: [[1.0516768 1.0413929]]
Q-values after update: [[1.0717245 1.0526878]]
Designated Priority: 3
Q-values before update: [[1.0699295 1.0690172]]
Q-values after update: [[1.07623   1.0501603]]
Episode 90 out of total 100, Total Reward: 21.0, Epsilon: 0.75, Current State: [-0.17141758 -1.7142504   0.25895366  2.476105  ], Steps Taken: 21
Designated Priority: 1
Q-values before update: [[1.052357  0.9388659]]
Q-values after update: [[1.056726  0.9317094]]
Designated Priority: 1
Q-values before update: [[1.0640595  0.93865293]]
Q-values after update: [[1.0668993  0.93161535]]
Designated Priority: 1
Q-values before update: [[1.0734911 0.9377139]]
Q-values after update: [[1.0749092 0.9307792]]
Designated Priority: 1
Q-values before update: [[1.0812285 0.9362849]]
Q-values after update: [[1.0835745  0.93260515]]
Designated Priority: 1
Q-values before update: [[1.0734437  0.92430836]]
Q-values after update: [[1.0743268 0.9206847]]
Designated Priority: 1
Q-values before update: [[1.0811582 0.926076 ]]
Q-values after update: [[1.0811852 0.9219179]]
Designated Priority: 1
Q-values before update: [[1.0861058 0.9321655]]
Q-values after update: [[1.087714  0.9316058]]
Designated Priority: 1
Q-values before update: [[1.0780456 0.917717 ]]
Q-values after update: [[1.0806491  0.92116356]]
Designated Priority: 1
Q-values before update: [[1.0698509 0.9139879]]
Q-values after update: [[1.0711159  0.91665804]]
Designated Priority: 1
Q-values before update: [[1.0792956 0.9226463]]
Q-values after update: [[1.0820905 0.928867 ]]
Designated Priority: 1
Q-values before update: [[1.0713738 0.9208056]]
Q-values after update: [[1.0750806 0.9294925]]
Designated Priority: 1
Q-values before update: [[1.065992  0.9213389]]
Q-values after update: [[1.06838   0.9286532]]
Designated Priority: 3
Q-values before update: [[1.0777332 0.9379933]]
Q-values after update: [[1.0676277 0.9398404]]
Episode 91 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.13581789 -0.6364886   0.2198106   1.312911  ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0708865  0.94074816]]
Q-values after update: [[1.0612314 0.9423243]]
Designated Priority: 1
Q-values before update: [[1.0690005  0.94902885]]
Q-values after update: [[1.0606949 0.9518112]]
Designated Priority: 1
Q-values before update: [[1.0515316 0.943954 ]]
Q-values after update: [[1.0431283  0.94606245]]
Designated Priority: 1
Q-values before update: [[1.0507174 0.9528128]]
Q-values after update: [[1.0423189 0.9544138]]
Designated Priority: 1
Q-values before update: [[1.0490787  0.96054006]]
Q-values after update: [[1.0410955 0.9618217]]
Designated Priority: 1
Q-values before update: [[1.0476166  0.96758986]]
Q-values after update: [[1.0403208  0.96868914]]
Designated Priority: 1
Q-values before update: [[1.0461774 0.9742761]]
Q-values after update: [[1.0399333  0.97534204]]
Designated Priority: 1
Q-values before update: [[1.0438704  0.98664224]]
Q-values after update: [[1.0391645 0.9880003]]
Designated Priority: 1
Q-values before update: [[1.042049   0.99966717]]
Q-values after update: [[1.0395392 1.0016433]]
Designated Priority: 1
Q-values before update: [[1.0419309 1.0130455]]
Q-values after update: [[1.0425884 1.0161532]]
Designated Priority: 1
Q-values before update: [[1.039767  1.0249909]]
Q-values after update: [[1.042661  1.0319357]]
Designated Priority: 1
Q-values before update: [[1.0292217 1.0129576]]
Q-values after update: [[1.0355204 1.0208338]]
Designated Priority: 3
Q-values before update: [[1.0331863 1.0315896]]
Q-values after update: [[1.027289  1.0333915]]
Episode 92 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.20404047 -1.7381972   0.25494963  2.7541916 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0019139 0.9644722]]
Q-values after update: [[0.9993683 0.966321 ]]
Designated Priority: 1
Q-values before update: [[1.0071604 0.9739957]]
Q-values after update: [[1.0053624  0.97589064]]
Designated Priority: 1
Q-values before update: [[1.0131085 0.9832592]]
Q-values after update: [[1.0121403  0.98525846]]
Designated Priority: 1
Q-values before update: [[1.0194681  0.99203515]]
Q-values after update: [[1.0193288  0.99421144]]
Designated Priority: 1
Q-values before update: [[1.0263803 1.0035288]]
Q-values after update: [[1.0273595 1.006076 ]]
Designated Priority: 1
Q-values before update: [[1.0317631 1.020161 ]]
Q-values after update: [[1.034219 1.023221]]
Designated Priority: 1
Q-values before update: [[1.0379276 1.0370817]]
Q-values after update: [[1.0423046 1.0409319]]
Designated Priority: 1
Q-values before update: [[1.042056  1.0530295]]
Q-values after update: [[1.0467603 1.0579679]]
Designated Priority: 1
Q-values before update: [[1.0342166 1.0376959]]
Q-values after update: [[1.0389602 1.0435097]]
Designated Priority: 3
Q-values before update: [[1.0268382 1.0245278]]
Q-values after update: [[1.0283358 1.023833 ]]
Episode 93 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.15928492 -0.83369356  0.22806904  1.3981293 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0025963  0.97946775]]
Q-values after update: [[1.0040139  0.97918665]]
Designated Priority: 1
Q-values before update: [[1.0133414  0.98840404]]
Q-values after update: [[1.0149187  0.98825717]]
Designated Priority: 1
Q-values before update: [[1.0241923 0.9970628]]
Q-values after update: [[1.0259235  0.99704427]]
Designated Priority: 1
Q-values before update: [[1.0354824 1.0053598]]
Q-values after update: [[1.0374115 1.005471 ]]
Designated Priority: 1
Q-values before update: [[1.0455077 1.0168648]]
Q-values after update: [[1.0476674 1.0170519]]
Designated Priority: 1
Q-values before update: [[1.0535116 1.0324354]]
Q-values after update: [[1.0560546 1.032837 ]]
Designated Priority: 1
Q-values before update: [[1.0611154 1.047865 ]]
Q-values after update: [[1.0643317 1.0486388]]
Designated Priority: 1
Q-values before update: [[1.0606865 1.0595803]]
Q-values after update: [[1.0655354 1.0612332]]
Designated Priority: 3
Q-values before update: [[1.0607654 1.0716257]]
Q-values after update: [[1.0523126 1.0496215]]
Episode 94 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.15764925 -1.3954217   0.2541564   2.3026364 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0159404 0.9684963]]
Q-values after update: [[1.0147322 0.9594009]]
Designated Priority: 1
Q-values before update: [[1.0237895  0.96743625]]
Q-values after update: [[1.0218737 0.9584657]]
Designated Priority: 1
Q-values before update: [[1.0299833 0.9651873]]
Q-values after update: [[1.0274801 0.9564024]]
Designated Priority: 1
Q-values before update: [[1.0350951 0.9615518]]
Q-values after update: [[1.0322232  0.95302606]]
Designated Priority: 1
Q-values before update: [[1.0388031 0.9566395]]
Q-values after update: [[1.0359261 0.9483554]]
Designated Priority: 1
Q-values before update: [[1.0388201  0.95604414]]
Q-values after update: [[1.0364151 0.9479197]]
Designated Priority: 1
Q-values before update: [[1.0359839 0.9550787]]
Q-values after update: [[1.0344813  0.94762313]]
Designated Priority: 1
Q-values before update: [[1.0258448 0.9502925]]
Q-values after update: [[1.0266117  0.94415164]]
Designated Priority: 3
Q-values before update: [[1.0162715 0.9454741]]
Q-values after update: [[1.0121634  0.93743056]]
Episode 95 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.11330026 -1.7144139   0.25002816  2.8166838 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0156637  0.92102414]]
Q-values after update: [[1.0149181  0.91753125]]
Designated Priority: 1
Q-values before update: [[1.0202904 0.9208391]]
Q-values after update: [[1.0194807 0.9174503]]
Designated Priority: 1
Q-values before update: [[1.0239978 0.9200424]]
Q-values after update: [[1.0233933 0.9168835]]
Designated Priority: 1
Q-values before update: [[1.0270634  0.91859645]]
Q-values after update: [[1.0268432 0.9157406]]
Designated Priority: 1
Q-values before update: [[1.0299478 0.9158658]]
Q-values after update: [[1.0304153 0.9134449]]
Designated Priority: 1
Q-values before update: [[1.03213   0.9136579]]
Q-values after update: [[1.0342233 0.9157752]]
Designated Priority: 1
Q-values before update: [[1.0233777  0.90767574]]
Q-values after update: [[1.0263338 0.9099602]]
Designated Priority: 1
Q-values before update: [[1.0279415 0.9109478]]
Q-values after update: [[1.0321269 0.9135998]]
Designated Priority: 1
Q-values before update: [[1.0309526  0.91774803]]
Q-values after update: [[1.0368344  0.92103934]]
Designated Priority: 1
Q-values before update: [[1.0260316  0.92046154]]
Q-values after update: [[1.0347099 0.9249543]]
Designated Priority: 3
Q-values before update: [[1.0224156 0.9236065]]
Q-values after update: [[1.0243986 0.9249716]]
Episode 96 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.18771045 -1.7275441   0.2333271   2.772141  ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0332363 0.916191 ]]
Q-values after update: [[1.0348092  0.91732126]]
Designated Priority: 1
Q-values before update: [[1.0409216  0.92084724]]
Q-values after update: [[1.0418143 0.9216857]]
Designated Priority: 1
Q-values before update: [[1.0469599 0.9243963]]
Q-values after update: [[1.0473855 0.925017 ]]
Designated Priority: 1
Q-values before update: [[1.0519435 0.926864 ]]
Q-values after update: [[1.052019  0.9273766]]
Designated Priority: 1
Q-values before update: [[1.055928   0.92730904]]
Q-values after update: [[1.0558972 0.9277351]]
Designated Priority: 1
Q-values before update: [[1.0573874  0.93018687]]
Q-values after update: [[1.0590277 0.9347991]]
Designated Priority: 1
Q-values before update: [[1.047845  0.9238144]]
Q-values after update: [[1.0495173 0.9277895]]
Designated Priority: 1
Q-values before update: [[1.0505486 0.9320073]]
Q-values after update: [[1.0527307  0.93611205]]
Designated Priority: 1
Q-values before update: [[1.0434597 0.9370749]]
Q-values after update: [[1.0470201 0.9416026]]
Designated Priority: 3
Q-values before update: [[1.0355223  0.94145477]]
Q-values after update: [[1.0297613 0.9414343]]
Episode 97 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.14341718 -1.5910058   0.24506     2.5924134 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0464859  0.93840545]]
Q-values after update: [[1.0448806 0.9413173]]
Designated Priority: 1
Q-values before update: [[1.038182  0.9365722]]
Q-values after update: [[1.0359092  0.93892074]]
Designated Priority: 1
Q-values before update: [[1.0435838 0.9445848]]
Q-values after update: [[1.0402776 0.9462198]]
Designated Priority: 1
Q-values before update: [[1.0462391 0.9501041]]
Q-values after update: [[1.0422862  0.95119727]]
Designated Priority: 1
Q-values before update: [[1.0474892  0.95429015]]
Q-values after update: [[1.0432063 0.9549686]]
Designated Priority: 1
Q-values before update: [[1.0471601 0.95706  ]]
Q-values after update: [[1.0428847 0.9574673]]
Designated Priority: 1
Q-values before update: [[1.0455933 0.958727 ]]
Q-values after update: [[1.0417333 0.95905  ]]
Designated Priority: 1
Q-values before update: [[1.0422149  0.96181864]]
Q-values after update: [[1.0397595 0.9647968]]
Designated Priority: 1
Q-values before update: [[1.0297906 0.9536538]]
Q-values after update: [[1.0282866  0.95644826]]
Designated Priority: 1
Q-values before update: [[1.0288409  0.95969707]]
Q-values after update: [[1.028532  0.9628203]]
Designated Priority: 1
Q-values before update: [[1.0226363  0.96661425]]
Q-values after update: [[1.0242001 0.9703609]]
Designated Priority: 1
Q-values before update: [[1.0109756 0.9697433]]
Q-values after update: [[1.0157541 0.974952 ]]
Designated Priority: 3
Q-values before update: [[1.0010355 0.9732245]]
Q-values after update: [[1.0053598  0.97804683]]
Episode 98 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.12010965 -1.7331568   0.2216322   2.7083166 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0215484 0.9618656]]
Q-values after update: [[1.0232394 0.9643577]]
Designated Priority: 1
Q-values before update: [[1.030038  0.9691956]]
Q-values after update: [[1.0322037 0.9727292]]
Designated Priority: 1
Q-values before update: [[1.0241685 0.9668816]]
Q-values after update: [[1.0255004  0.96972096]]
Designated Priority: 1
Q-values before update: [[1.0327759 0.974954 ]]
Q-values after update: [[1.0338053  0.97756064]]
Designated Priority: 1
Q-values before update: [[1.0400743 0.9819492]]
Q-values after update: [[1.0408642  0.98433757]]
Designated Priority: 1
Q-values before update: [[1.046144  0.9878814]]
Q-values after update: [[1.046835  0.9901025]]
Designated Priority: 1
Q-values before update: [[1.0511013 0.9929452]]
Q-values after update: [[1.051877   0.99507725]]
Designated Priority: 1
Q-values before update: [[1.0532746 1.0016825]]
Q-values after update: [[1.0544347 1.0038825]]
Designated Priority: 1
Q-values before update: [[1.0495737 1.0087935]]
Q-values after update: [[1.0518422 1.0114136]]
Designated Priority: 1
Q-values before update: [[1.0403872 1.0121818]]
Q-values after update: [[1.0448067 1.0158032]]
Designated Priority: 3
Q-values before update: [[1.0318378 1.015637 ]]
Q-values after update: [[1.0269969 1.0143611]]
Episode 99 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.10754546 -1.7953005   0.22332436  2.7728148 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0320736 0.9864282]]
Q-values after update: [[1.0294856 0.9864033]]
Designated Priority: 1
Q-values before update: [[1.0372691  0.99234843]]
Q-values after update: [[1.0344257 0.9920708]]
Designated Priority: 1
Q-values before update: [[1.0408418 0.9968034]]
Q-values after update: [[1.0379705  0.99637365]]
Designated Priority: 1
Q-values before update: [[1.0431149 1.0000021]]
Q-values after update: [[1.0405145  0.99955654]]
Designated Priority: 1
Q-values before update: [[1.044398  1.0022542]]
Q-values after update: [[1.0424088 1.0019624]]
Designated Priority: 1
Q-values before update: [[1.0432556 1.0078927]]
Q-values after update: [[1.0423225 1.0080217]]
Designated Priority: 1
Q-values before update: [[1.0400635 1.0135243]]
Q-values after update: [[1.0407671 1.0143795]]
Designated Priority: 1
Q-values before update: [[1.0281627 1.0149575]]
Q-values after update: [[1.0318501 1.0172896]]
Designated Priority: 1
Q-values before update: [[1.0176553 1.0163864]]
Q-values after update: [[1.0258602 1.0211511]]
Designated Priority: 3
Q-values before update: [[1.0102811 1.0192392]]
Q-values after update: [[1.0148422 1.0220709]]
Episode 100 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.15273032 -1.9942698   0.24151158  3.0273144 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0244868 0.9868069]]
Q-values after update: [[1.0263388 0.9877976]]
Designated Priority: 1
Q-values before update: [[1.0346766 0.9941776]]
Q-values after update: [[1.0360594  0.99503195]]
Designated Priority: 1
Q-values before update: [[1.0433637 1.0004936]]
Q-values after update: [[1.0443426 1.0012192]]
Designated Priority: 1
Q-values before update: [[1.0506296 1.0057712]]
Q-values after update: [[1.051305  1.0063889]]
Designated Priority: 1
Q-values before update: [[1.0565884 1.0100362]]
Q-values after update: [[1.0571177 1.0105965]]
Designated Priority: 1
Q-values before update: [[1.0597979 1.0171978]]
Q-values after update: [[1.0604697 1.0178016]]
Designated Priority: 1
Q-values before update: [[1.0572598 1.0242028]]
Q-values after update: [[1.0587628 1.0251979]]
Designated Priority: 1
Q-values before update: [[1.0476937 1.0271761]]
Q-values after update: [[1.0501833 1.0301572]]
Designated Priority: 1
Q-values before update: [[1.03899   1.0127541]]
Q-values after update: [[1.0428432 1.0161593]]
Designated Priority: 3
Q-values before update: [[1.0318085 1.0186429]]
Q-values after update: [[1.0272658 1.0175574]]
Episode 1 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.1441223  -1.5602064   0.25105178  2.5243902 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0337485 0.9981177]]
Q-values after update: [[1.0309087 0.9979259]]
Designated Priority: 1
Q-values before update: [[1.0395503 1.004724 ]]
Q-values after update: [[1.0365374 1.0043375]]
Designated Priority: 1
Q-values before update: [[1.0438719 1.0100164]]
Q-values after update: [[1.040915  1.0095348]]
Designated Priority: 1
Q-values before update: [[1.0469973 1.0141265]]
Q-values after update: [[1.044363 1.013671]]
Designated Priority: 1
Q-values before update: [[1.0492464 1.0172064]]
Q-values after update: [[1.047236  1.0169291]]
Designated Priority: 1
Q-values before update: [[1.0492063 1.023544 ]]
Q-values after update: [[1.0482234 1.0237062]]
Designated Priority: 1
Q-values before update: [[1.047719  1.0312403]]
Q-values after update: [[1.0482563 1.0320947]]
Designated Priority: 1
Q-values before update: [[1.0363948 1.0335718]]
Q-values after update: [[1.0398763 1.0359067]]
Designated Priority: 1
Q-values before update: [[1.0263364 1.0363425]]
Q-values after update: [[1.0313737 1.0418255]]
Designated Priority: 3
Q-values before update: [[1.018647  1.0228082]]
Q-values after update: [[1.0197786 1.0214409]]
Episode 2 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.18764073 -1.1966741   0.2264456   1.8964106 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0200143 0.994249 ]]
Q-values after update: [[1.0208151  0.99333715]]
Designated Priority: 1
Q-values before update: [[1.0298945 1.0005779]]
Q-values after update: [[1.0305463 0.9997068]]
Designated Priority: 1
Q-values before update: [[1.038429  1.0058427]]
Q-values after update: [[1.0389997 1.0050296]]
Designated Priority: 1
Q-values before update: [[1.0457188 1.0100878]]
Q-values after update: [[1.046315 1.009369]]
Designated Priority: 1
Q-values before update: [[1.0519013 1.0133737]]
Q-values after update: [[1.0526875 1.0128183]]
Designated Priority: 1
Q-values before update: [[1.0550894 1.0204641]]
Q-values after update: [[1.056421  1.0201602]]
Designated Priority: 1
Q-values before update: [[1.0506027 1.0252998]]
Q-values after update: [[1.0532217 1.0257051]]
Designated Priority: 1
Q-values before update: [[1.0414797 1.0273912]]
Q-values after update: [[1.0452636 1.030338 ]]
Designated Priority: 3
Q-values before update: [[1.0330467 1.0122887]]
Q-values after update: [[1.0284604 1.0107992]]
Episode 3 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.15280445 -1.4029127   0.2244763   2.2331157 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0310186 0.9946438]]
Q-values after update: [[1.0277438 0.9939853]]
Designated Priority: 1
Q-values before update: [[1.0368978 1.0011495]]
Q-values after update: [[1.0330788 1.000177 ]]
Designated Priority: 1
Q-values before update: [[1.0408176 1.0061173]]
Q-values after update: [[1.0366848 1.0049199]]
Designated Priority: 1
Q-values before update: [[1.0430518 1.0096593]]
Q-values after update: [[1.038883  1.0083473]]
Designated Priority: 1
Q-values before update: [[1.0439159 1.0119092]]
Q-values after update: [[1.0400426 1.0106282]]
Designated Priority: 1
Q-values before update: [[1.040653  1.0187355]]
Q-values after update: [[1.0375408 1.0177889]]
Designated Priority: 1
Q-values before update: [[1.0268615 1.0201979]]
Q-values after update: [[1.0255414 1.0200416]]
Designated Priority: 1
Q-values before update: [[1.0121475 1.0207133]]
Q-values after update: [[1.0119314 1.0225344]]
Designated Priority: 3
Q-values before update: [[1.0008858 1.0046457]]
Q-values after update: [[1.000097  1.0050814]]
Episode 4 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.09425224 -0.9798435   0.23043603  1.7043065 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0055412 0.9914057]]
Q-values after update: [[1.0049055  0.99196255]]
Designated Priority: 1
Q-values before update: [[0.9972573 0.9857676]]
Q-values after update: [[0.9968115  0.98628885]]
Designated Priority: 1
Q-values before update: [[1.0055032 0.9934379]]
Q-values after update: [[1.0053777 0.9940359]]
Designated Priority: 1
Q-values before update: [[1.0133266 1.0003915]]
Q-values after update: [[1.0135798 1.0010853]]
Designated Priority: 1
Q-values before update: [[1.0207773 1.0068452]]
Q-values after update: [[1.0215046 1.0076872]]
Designated Priority: 1
Q-values before update: [[1.0275539 1.0124097]]
Q-values after update: [[1.0288801 1.0134666]]
Designated Priority: 1
Q-values before update: [[1.0338287 1.0171839]]
Q-values after update: [[1.0353789 1.0189538]]
Designated Priority: 1
Q-values before update: [[1.0219952 1.007539 ]]
Q-values after update: [[1.0241733 1.0094142]]
Designated Priority: 1
Q-values before update: [[1.0295403 1.0134871]]
Q-values after update: [[1.0326159 1.015718 ]]
Designated Priority: 1
Q-values before update: [[1.034605  1.0228717]]
Q-values after update: [[1.0388823 1.025636 ]]
Designated Priority: 1
Q-values before update: [[1.0332742 1.0311685]]
Q-values after update: [[1.0395505 1.0349139]]
Designated Priority: 1
Q-values before update: [[1.027496  1.0367295]]
Q-values after update: [[1.0345495 1.042526 ]]
Designated Priority: 3
Q-values before update: [[1.0223193 1.0238447]]
Q-values after update: [[1.0255218 1.0230072]]
Episode 5 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.18926018 -0.93592286  0.21427599  1.6144503 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0226151 1.0022367]]
Q-values after update: [[1.0250752 1.001655 ]]
Designated Priority: 1
Q-values before update: [[1.0350658 1.0098536]]
Q-values after update: [[1.0372231 1.0092874]]
Designated Priority: 1
Q-values before update: [[1.0459747 1.0163213]]
Q-values after update: [[1.0478315 1.0157578]]
Designated Priority: 1
Q-values before update: [[1.0553718 1.0216545]]
Q-values after update: [[1.0572462 1.0215427]]
Designated Priority: 1
Q-values before update: [[1.0437171 1.0103072]]
Q-values after update: [[1.0453049 1.0101701]]
Designated Priority: 1
Q-values before update: [[1.053107 1.016192]]
Q-values after update: [[1.0545689 1.0160733]]
Designated Priority: 1
Q-values before update: [[1.0611526 1.0209606]]
Q-values after update: [[1.0626053 1.0209067]]
Designated Priority: 1
Q-values before update: [[1.0657212 1.0295101]]
Q-values after update: [[1.0675019 1.0295972]]
Designated Priority: 1
Q-values before update: [[1.0584832 1.0332291]]
Q-values after update: [[1.0615374 1.0340215]]
Designated Priority: 3
Q-values before update: [[1.0497922 1.0359832]]
Q-values after update: [[1.0389233 1.0293831]]
Episode 6 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.16464755 -1.5999646   0.21322623  2.5001795 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0373498 1.0020509]]
Q-values after update: [[1.0320234  0.99961996]]
Designated Priority: 1
Q-values before update: [[1.0412308 1.0069253]]
Q-values after update: [[1.0357602 1.0042715]]
Designated Priority: 1
Q-values before update: [[1.0432067 1.0100266]]
Q-values after update: [[1.0379047 1.0073051]]
Designated Priority: 1
Q-values before update: [[1.0436774 1.011569 ]]
Q-values after update: [[1.0389194 1.0089668]]
Designated Priority: 1
Q-values before update: [[1.0431005 1.0117949]]
Q-values after update: [[1.0393023 1.009536 ]]
Designated Priority: 1
Q-values before update: [[1.0401001 1.0150746]]
Q-values after update: [[1.0377766 1.0134864]]
Designated Priority: 1
Q-values before update: [[1.0284933 1.0158297]]
Q-values after update: [[1.0269684 1.0165006]]
Designated Priority: 1
Q-values before update: [[1.0192816 1.0008881]]
Q-values after update: [[1.0204829 1.0026714]]
Designated Priority: 1
Q-values before update: [[1.0066088 1.0028363]]
Q-values after update: [[1.0116034 1.0064551]]
Designated Priority: 3
Q-values before update: [[0.9957863 1.0053374]]
Q-values after update: [[0.9997524 1.0073719]]
Episode 7 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.18679768 -1.2135581   0.2218976   1.9079038 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0227532  0.99859095]]
Q-values after update: [[1.0250807  0.99962854]]
Designated Priority: 1
Q-values before update: [[1.0331111 1.0059645]]
Q-values after update: [[1.0350735 1.0068942]]
Designated Priority: 1
Q-values before update: [[1.0418937 1.0121297]]
Q-values after update: [[1.0435679 1.0129703]]
Designated Priority: 1
Q-values before update: [[1.0491993 1.0171189]]
Q-values after update: [[1.0507121 1.0179114]]
Designated Priority: 1
Q-values before update: [[1.0551739 1.0209836]]
Q-values after update: [[1.0567074 1.0218014]]
Designated Priority: 1
Q-values before update: [[1.0581039 1.0271928]]
Q-values after update: [[1.0600035 1.0281588]]
Designated Priority: 1
Q-values before update: [[1.0526245 1.0318271]]
Q-values after update: [[1.0557413 1.0334145]]
Designated Priority: 1
Q-values before update: [[1.0415106 1.0331008]]
Q-values after update: [[1.0471029 1.0360175]]
Designated Priority: 1
Q-values before update: [[1.0310457 1.0344954]]
Q-values after update: [[1.0381356 1.0405029]]
Designated Priority: 3
Q-values before update: [[1.0242674 1.0204793]]
Q-values after update: [[1.0236831 1.0219957]]
Episode 8 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.19049756 -1.5310555   0.23676647  2.4888656 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0348194 1.0033221]]
Q-values after update: [[1.0339485 1.0041928]]
Designated Priority: 1
Q-values before update: [[1.0434482 1.0118216]]
Q-values after update: [[1.0425425 1.0123023]]
Designated Priority: 1
Q-values before update: [[1.0321006 1.0037146]]
Q-values after update: [[1.0307612 1.0039086]]
Designated Priority: 1
Q-values before update: [[1.0402672 1.0116022]]
Q-values after update: [[1.0385568 1.0116091]]
Designated Priority: 1
Q-values before update: [[1.0466728 1.0180786]]
Q-values after update: [[1.0451088 1.0180627]]
Designated Priority: 1
Q-values before update: [[1.0333488 1.0081626]]
Q-values after update: [[1.031905  1.0080075]]
Designated Priority: 1
Q-values before update: [[1.0215724 0.9993527]]
Q-values after update: [[1.0201466 0.9991443]]
Designated Priority: 1
Q-values before update: [[1.0296655 1.0069203]]
Q-values after update: [[1.0282083 1.0066812]]
Designated Priority: 1
Q-values before update: [[1.0363135 1.0131922]]
Q-values after update: [[1.0349166 1.012956 ]]
Designated Priority: 1
Q-values before update: [[1.0416478 1.0182261]]
Q-values after update: [[1.0405098 1.0183464]]
Designated Priority: 1
Q-values before update: [[1.0274994 1.0071142]]
Q-values after update: [[1.0267255 1.0073042]]
Designated Priority: 1
Q-values before update: [[1.0332538 1.012804 ]]
Q-values after update: [[1.0329651 1.0131764]]
Designated Priority: 1
Q-values before update: [[1.0369538 1.0182033]]
Q-values after update: [[1.0374038 1.018901 ]]
Designated Priority: 1
Q-values before update: [[1.0274891 1.0225831]]
Q-values after update: [[1.0296402 1.0240946]]
Designated Priority: 3
Q-values before update: [[1.0163786 1.0256375]]
Q-values after update: [[1.0150945 1.0205061]]
Episode 9 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [-0.15250666 -0.95441276  0.22011843  1.7617569 ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[1.028019  1.0064782]]
Q-values after update: [[1.0271689 1.0032578]]
Designated Priority: 1
Q-values before update: [[1.0365835 1.0109367]]
Q-values after update: [[1.0350261 1.0076084]]
Designated Priority: 1
Q-values before update: [[1.0429308 1.013854 ]]
Q-values after update: [[1.0408487 1.0104785]]
Designated Priority: 1
Q-values before update: [[1.0472825 1.0153301]]
Q-values after update: [[1.0449092 1.011985 ]]
Designated Priority: 1
Q-values before update: [[1.0499051 1.0154719]]
Q-values after update: [[1.0478114 1.0126895]]
Designated Priority: 1
Q-values before update: [[1.0340765 1.001195 ]]
Q-values after update: [[1.0325044 0.9993677]]
Designated Priority: 1
Q-values before update: [[1.0203261 0.9892588]]
Q-values after update: [[1.0191703  0.98777395]]
Designated Priority: 1
Q-values before update: [[1.0254864 0.9922574]]
Q-values after update: [[1.0247456  0.99099505]]
Designated Priority: 1
Q-values before update: [[1.0288378 0.9945418]]
Q-values after update: [[1.0287895 0.9936222]]
Designated Priority: 1
Q-values before update: [[1.0190852 0.9949323]]
Q-values after update: [[1.0206249 0.9947477]]
Designated Priority: 3
Q-values before update: [[1.0066537 0.9946729]]
Q-values after update: [[1.0065265 0.9937122]]
Episode 10 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.10290114 -1.3384364   0.21574816  2.268571  ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0212202 0.9892695]]
Q-values after update: [[1.0210388 0.988655 ]]
Designated Priority: 1
Q-values before update: [[1.0295644 0.9951993]]
Q-values after update: [[1.0291992 0.9945446]]
Designated Priority: 1
Q-values before update: [[1.0363326 0.9998193]]
Q-values after update: [[1.0359303 0.9991791]]
Designated Priority: 1
Q-values before update: [[1.0417111 1.0032113]]
Q-values after update: [[1.0414629 1.0026634]]
Designated Priority: 1
Q-values before update: [[1.0458332 1.0055958]]
Q-values after update: [[1.0460759 1.0062126]]
Designated Priority: 1
Q-values before update: [[1.0324081  0.99483657]]
Q-values after update: [[1.0330466  0.99555075]]
Designated Priority: 1
Q-values before update: [[1.0377674 0.9985188]]
Q-values after update: [[1.0390363 0.9994901]]
Designated Priority: 1
Q-values before update: [[1.0361446 1.0034891]]
Q-values after update: [[1.0386531 1.0049912]]
Designated Priority: 1
Q-values before update: [[1.024988  1.0049049]]
Q-values after update: [[1.0299536 1.0076385]]
Designated Priority: 3
Q-values before update: [[1.0143365 1.0061712]]
Q-values after update: [[1.0151411 1.0067269]]
Episode 11 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.12484142 -1.6071888   0.21327706  2.5043838 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0310974  0.99695385]]
Q-values after update: [[1.0315297  0.99736357]]
Designated Priority: 1
Q-values before update: [[1.0400604 1.003905 ]]
Q-values after update: [[1.0402514 1.0042027]]
Designated Priority: 1
Q-values before update: [[1.0474691 1.0095656]]
Q-values after update: [[1.0475464 1.0098   ]]
Designated Priority: 1
Q-values before update: [[1.0534866 1.014005 ]]
Q-values after update: [[1.0536456 1.0142565]]
Designated Priority: 1
Q-values before update: [[1.0583411 1.0173218]]
Q-values after update: [[1.0588261 1.0177045]]
Designated Priority: 1
Q-values before update: [[1.0609919 1.0223472]]
Q-values after update: [[1.062172  1.0230373]]
Designated Priority: 1
Q-values before update: [[1.0578084 1.0271785]]
Q-values after update: [[1.0599043 1.0299046]]
Designated Priority: 1
Q-values before update: [[1.0493511 1.0123057]]
Q-values after update: [[1.0524044 1.0152206]]
Designated Priority: 1
Q-values before update: [[1.0414287 1.01653  ]]
Q-values after update: [[1.0469471 1.020632 ]]
Designated Priority: 1
Q-values before update: [[1.032387  1.0198593]]
Q-values after update: [[1.0418288 1.026042 ]]
Designated Priority: 3
Q-values before update: [[1.0255432 1.0241872]]
Q-values after update: [[1.0263135 1.0255297]]
Episode 12 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.22241968 -1.7794328   0.23030478  2.7648964 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.051296 1.011586]]
Q-values after update: [[1.0508623 1.0122219]]
Designated Priority: 1
Q-values before update: [[1.060684  1.0199165]]
Q-values after update: [[1.0588701 1.0199537]]
Designated Priority: 1
Q-values before update: [[1.0673257 1.0264435]]
Q-values after update: [[1.0643276 1.0259385]]
Designated Priority: 1
Q-values before update: [[1.0714335 1.0312264]]
Q-values after update: [[1.0675198 1.0302584]]
Designated Priority: 1
Q-values before update: [[1.07322   1.0344092]]
Q-values after update: [[1.0687354 1.0330937]]
Designated Priority: 1
Q-values before update: [[1.0714824 1.0390142]]
Q-values after update: [[1.0673444 1.0377982]]
Designated Priority: 1
Q-values before update: [[1.0527778 1.0208043]]
Q-values after update: [[1.0493642 1.020123 ]]
Designated Priority: 1
Q-values before update: [[1.0346751 1.0076818]]
Q-values after update: [[1.031891  1.0071914]]
Designated Priority: 1
Q-values before update: [[1.0377809 1.0114837]]
Q-values after update: [[1.0356946 1.0112308]]
Designated Priority: 1
Q-values before update: [[1.030566 1.014599]]
Q-values after update: [[1.029968 1.014986]]
Designated Priority: 1
Q-values before update: [[1.0166659 1.0155114]]
Q-values after update: [[1.0171423 1.0178795]]
Designated Priority: 3
Q-values before update: [[1.006527  1.0004689]]
Q-values after update: [[1.006844  1.0023878]]
Episode 13 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.12809503 -0.7625626   0.2240319   1.4085798 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.0260965 1.0108767]]
Q-values after update: [[1.0251278 1.0117099]]
Designated Priority: 1
Q-values before update: [[1.0346841 1.0195397]]
Q-values after update: [[1.0336461 1.0197461]]
Designated Priority: 1
Q-values before update: [[1.0222325 1.0102199]]
Q-values after update: [[1.0206981 1.010123 ]]
Designated Priority: 1
Q-values before update: [[1.030467  1.0181972]]
Q-values after update: [[1.0286055 1.0179676]]
Designated Priority: 1
Q-values before update: [[1.0371099 1.024892 ]]
Q-values after update: [[1.0350622 1.0245748]]
Designated Priority: 1
Q-values before update: [[1.0423414 1.0303719]]
Q-values after update: [[1.0402975 1.0300341]]
Designated Priority: 1
Q-values before update: [[1.0462768 1.0348204]]
Q-values after update: [[1.044313  1.0341946]]
Designated Priority: 1
Q-values before update: [[1.029432  1.0210257]]
Q-values after update: [[1.0279285 1.0205628]]
Designated Priority: 1
Q-values before update: [[1.0343295 1.025506 ]]
Q-values after update: [[1.0330102 1.02516  ]]
Designated Priority: 1
Q-values before update: [[1.0182989 1.0122432]]
Q-values after update: [[1.0177302 1.0121809]]
Designated Priority: 1
Q-values before update: [[1.0243745 1.0173031]]
Q-values after update: [[1.0247219 1.0176572]]
Designated Priority: 1
Q-values before update: [[1.0225857 1.0232539]]
Q-values after update: [[1.023334  1.0244427]]
Designated Priority: 1
Q-values before update: [[1.0141784 1.0090225]]
Q-values after update: [[1.0160835 1.0105752]]
Designated Priority: 1
Q-values before update: [[1.0064802 1.0130837]]
Q-values after update: [[1.0090134 1.0160632]]
Designated Priority: 3
Q-values before update: [[0.9995439  0.99951607]]
Q-values after update: [[1.0018109 1.0020621]]
Episode 14 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [-0.11701234 -0.95416445  0.23083219  1.7190483 ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[1.0050229 1.0048809]]
Q-values after update: [[1.0065935 1.0065545]]
Designated Priority: 1
Q-values before update: [[1.0173616 1.0157542]]
Q-values after update: [[1.0187321 1.0169059]]
Designated Priority: 1
Q-values before update: [[1.0066221 1.0064332]]
Q-values after update: [[1.0079676 1.007446 ]]
Designated Priority: 1
Q-values before update: [[1.0189914 1.0168917]]
Q-values after update: [[1.0204786 1.0179754]]
Designated Priority: 1
Q-values before update: [[1.0303086 1.0263026]]
Q-values after update: [[1.0316013 1.0269836]]
Designated Priority: 1
Q-values before update: [[1.0179574 1.0150363]]
Q-values after update: [[1.0192475 1.0156593]]
Designated Priority: 1
Q-values before update: [[1.0293496 1.0242124]]
Q-values after update: [[1.0304848 1.0245636]]
Designated Priority: 1
Q-values before update: [[1.0167876 1.0125422]]
Q-values after update: [[1.0176765 1.0126022]]
Designated Priority: 1
Q-values before update: [[1.0052669 1.0017718]]
Q-values after update: [[1.0063384 1.0019102]]
Designated Priority: 1
Q-values before update: [[1.0179747 1.0118339]]
Q-values after update: [[1.0192212 1.0120921]]
Designated Priority: 1
Q-values before update: [[1.0295857 1.0208106]]
Q-values after update: [[1.030947 1.021163]]
Designated Priority: 1
Q-values before update: [[1.0400858 1.0287135]]
Q-values after update: [[1.0415635 1.0291619]]
Designated Priority: 1
Q-values before update: [[1.048661  1.0365067]]
Q-values after update: [[1.0500801 1.0370514]]
Designated Priority: 1
Q-values before update: [[1.0345283 1.0214862]]
Q-values after update: [[1.0362575 1.0221543]]
Designated Priority: 1
Q-values before update: [[1.0388097 1.02883  ]]
Q-values after update: [[1.0413051 1.029911 ]]
Designated Priority: 3
Q-values before update: [[1.0318401 1.0345392]]
Q-values after update: [[1.0300359 1.0270122]]
Episode 15 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [-0.12899883 -0.8332193   0.21875     1.5130829 ], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[1.022569  1.0055969]]
Q-values after update: [[1.0218748 1.0007632]]
Designated Priority: 1
Q-values before update: [[1.0335371 1.0104415]]
Q-values after update: [[1.0322474 1.0056382]]
Designated Priority: 1
Q-values before update: [[1.0423837 1.0138041]]
Q-values after update: [[1.0405961 1.0090604]]
Designated Priority: 1
Q-values before update: [[1.0492545 1.0157703]]
Q-values after update: [[1.0471141 1.0111287]]
Designated Priority: 1
Q-values before update: [[1.0541624 1.016572 ]]
Q-values after update: [[1.0518916 1.0121124]]
Designated Priority: 1
Q-values before update: [[1.0507622 1.0183696]]
Q-values after update: [[1.0489231 1.0141821]]
Designated Priority: 1
Q-values before update: [[1.036862  1.0155469]]
Q-values after update: [[1.0367787 1.0124383]]
Designated Priority: 3
Q-values before update: [[1.0225203 1.0121528]]
Q-values after update: [[1.015976  1.0058639]]
Episode 16 out of total 100, Total Reward: 8.0, Epsilon: 0.75, Current State: [-0.08696737 -1.6090877   0.21273355  2.5347078 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[1.0144467  0.97809696]]
Q-values after update: [[1.0110763 0.9749072]]
Designated Priority: 1
Q-values before update: [[1.0211164  0.98258215]]
Q-values after update: [[1.0174886  0.97932655]]
Designated Priority: 1
Q-values before update: [[1.025933   0.98553485]]
Q-values after update: [[1.0222447  0.98229945]]
Designated Priority: 1
Q-values before update: [[1.0291605 0.9870913]]
Q-values after update: [[1.0256689  0.98398685]]
Designated Priority: 1
Q-values before update: [[1.0310377  0.98746973]]
Q-values after update: [[1.0280635 0.9846462]]
Designated Priority: 1
Q-values before update: [[1.0260823 0.9881623]]
Q-values after update: [[1.0241112 0.9858192]]
Designated Priority: 1
Q-values before update: [[1.0099789  0.98501897]]
Q-values after update: [[1.0105231 0.9839566]]
Designated Priority: 1
Q-values before update: [[0.9942015 0.9815687]]
Q-values after update: [[0.99893844 0.9827566 ]]
Designated Priority: 3
Q-values before update: [[0.9808339 0.9790801]]
Q-values after update: [[0.99123055 0.9834737 ]]
Episode 17 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.10084703 -1.7202129   0.23901992  2.843316  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0060258  0.96411663]]
Q-values after update: [[1.0112045 0.9664919]]
Designated Priority: 1
Q-values before update: [[1.0022044 0.9595473]]
Q-values after update: [[1.006368  0.9612732]]
Designated Priority: 1
Q-values before update: [[1.0172312 0.9698565]]
Q-values after update: [[1.0213559  0.97175294]]
Designated Priority: 1
Q-values before update: [[1.0319608 0.9796115]]
Q-values after update: [[1.0362647  0.98228335]]
Designated Priority: 1
Q-values before update: [[1.0239422 0.972968 ]]
Q-values after update: [[1.0279534  0.97630364]]
Designated Priority: 1
Q-values before update: [[1.0171099 0.9678684]]
Q-values after update: [[1.0198765 0.9703704]]
Designated Priority: 1
Q-values before update: [[1.0324744  0.98036695]]
Q-values after update: [[1.0347822 0.9827267]]
Designated Priority: 1
Q-values before update: [[1.0464993 0.9914695]]
Q-values after update: [[1.0489265 0.9941238]]
Designated Priority: 1
Q-values before update: [[1.0355582 0.9839583]]
Q-values after update: [[1.0378456  0.98699886]]
Designated Priority: 1
Q-values before update: [[1.0257441 0.9775298]]
Q-values after update: [[1.0268476 0.9798082]]
Designated Priority: 1
Q-values before update: [[1.0405127  0.99067706]]
Q-values after update: [[1.040907  0.9925919]]
Designated Priority: 1
Q-values before update: [[1.0533799 1.0019927]]
Q-values after update: [[1.0529748 1.0034976]]
Designated Priority: 1
Q-values before update: [[1.0642462 1.011822 ]]
Q-values after update: [[1.0630524 1.0129049]]
Designated Priority: 1
Q-values before update: [[1.0731422 1.0201564]]
Q-values after update: [[1.0712202 1.020818 ]]
Designated Priority: 1
Q-values before update: [[1.0800647 1.027055 ]]
Q-values after update: [[1.0775347 1.0273166]]
Designated Priority: 1
Q-values before update: [[1.0842814 1.0343363]]
Q-values after update: [[1.0813959 1.0342695]]
Designated Priority: 1
Q-values before update: [[1.0810721 1.0405644]]
Q-values after update: [[1.0785747 1.0405633]]
Designated Priority: 1
Q-values before update: [[1.0688283 1.0421289]]
Q-values after update: [[1.067976  1.0428256]]
Designated Priority: 3
Q-values before update: [[1.0560876 1.0430942]]
Q-values after update: [[1.0372112 1.0337124]]
Episode 18 out of total 100, Total Reward: 19.0, Epsilon: 0.75, Current State: [-0.14524803 -1.7881114   0.21110699  2.7642817 ], Steps Taken: 19
Designated Priority: 1
Q-values before update: [[1.0242239  0.99760175]]
Q-values after update: [[1.0145335  0.99458575]]
Designated Priority: 1
Q-values before update: [[1.0254182 1.0028898]]
Q-values after update: [[1.0157305 0.999521 ]]
Designated Priority: 1
Q-values before update: [[1.0246795 1.0061095]]
Q-values after update: [[1.0154315 1.002615 ]]
Designated Priority: 1
Q-values before update: [[1.0225786 1.0075674]]
Q-values after update: [[1.0142326 1.0041906]]
Designated Priority: 1
Q-values before update: [[1.0195347 1.0077153]]
Q-values after update: [[1.0119051 1.0050167]]
Designated Priority: 1
Q-values before update: [[0.99821913 0.9933435 ]]
Q-values after update: [[0.9930102  0.99172187]]
Designated Priority: 1
Q-values before update: [[0.9979305  0.99464333]]
Q-values after update: [[0.9934341 0.9941533]]
Designated Priority: 1
Q-values before update: [[0.98046476 0.98312455]]
Q-values after update: [[0.97713876 0.98410094]]
Designated Priority: 1
Q-values before update: [[0.9657209  0.97446764]]
Q-values after update: [[0.9633833  0.97676754]]
Designated Priority: 1
Q-values before update: [[0.9536817  0.96872914]]
Q-values after update: [[0.9520618  0.97188044]]
Designated Priority: 1
Q-values before update: [[0.9440937  0.96552193]]
Q-values after update: [[0.9432218 0.9698731]]
Designated Priority: 1
Q-values before update: [[0.93693924 0.96486974]]
Q-values after update: [[0.93670785 0.9703163 ]]
Designated Priority: 1
Q-values before update: [[0.93217516 0.9667965 ]]
Q-values after update: [[0.9324968 0.973171 ]]
Designated Priority: 1
Q-values before update: [[0.93022966 0.9720874 ]]
Q-values after update: [[0.9311696 0.9795437]]
Designated Priority: 1
Q-values before update: [[0.9300026 0.978673 ]]
Q-values after update: [[0.93159264 0.98726803]]
Designated Priority: 1
Q-values before update: [[0.9311948 0.9871344]]
Q-values after update: [[0.9356916  0.99635994]]
Designated Priority: 1
Q-values before update: [[0.94353914 1.003191  ]]
Q-values after update: [[0.947688  1.0122496]]
Designated Priority: 1
Q-values before update: [[0.9472913 1.0121014]]
Q-values after update: [[0.9516035 1.021432 ]]
Designated Priority: 1
Q-values before update: [[0.9520817 1.0221542]]
Q-values after update: [[0.95658815 1.0318027 ]]
Designated Priority: 1
Q-values before update: [[0.9579207 1.0334018]]
Q-values after update: [[0.9654919 1.044083 ]]
Designated Priority: 1
Q-values before update: [[0.9748951 1.0535029]]
Q-values after update: [[0.9812565 1.0624475]]
Designated Priority: 1
Q-values before update: [[0.9827673 1.0642132]]
Q-values after update: [[0.98844945 1.0717422 ]]
Designated Priority: 1
Q-values before update: [[0.99102294 1.0745771 ]]
Q-values after update: [[0.99565387 1.0802255 ]]
Designated Priority: 1
Q-values before update: [[0.9957626 1.0793965]]
Q-values after update: [[0.99908936 1.0827131 ]]
Designated Priority: 3
Q-values before update: [[0.9977923 1.0798421]]
Q-values after update: [[0.9782981 1.0432734]]
Episode 19 out of total 100, Total Reward: 25.0, Epsilon: 0.75, Current State: [ 0.25165227  2.1403596  -0.21587019 -2.895404  ], Steps Taken: 25
Designated Priority: 1
Q-values before update: [[0.9949278 1.0683613]]
Q-values after update: [[0.99191713 1.0557374 ]]
Designated Priority: 1
Q-values before update: [[0.98612845 1.0497336 ]]
Q-values after update: [[0.9821454 1.036175 ]]
Designated Priority: 1
Q-values before update: [[0.9757816 1.0295883]]
Q-values after update: [[0.9713706 1.016273 ]]
Designated Priority: 1
Q-values before update: [[0.9651555 1.0094998]]
Q-values after update: [[0.9607695  0.99741316]]
Designated Priority: 1
Q-values before update: [[0.95469624 0.99047625]]
Q-values after update: [[0.9508318 0.9805496]]
Designated Priority: 1
Q-values before update: [[0.94493   0.9735137]]
Q-values after update: [[0.9439765 0.9654232]]
Designated Priority: 1
Q-values before update: [[0.9583725 0.9805144]]
Q-values after update: [[0.9586562  0.97571534]]
Designated Priority: 1
Q-values before update: [[0.9497267 0.9647689]]
Q-values after update: [[0.9507835 0.9627186]]
Designated Priority: 1
Q-values before update: [[0.9375347 0.9459659]]
Q-values after update: [[0.94057167 0.948601  ]]
Designated Priority: 1
Q-values before update: [[0.924304  0.9263141]]
Q-values after update: [[0.9334109 0.9327262]]
Designated Priority: 3
Q-values before update: [[0.95303786 0.95705223]]
Q-values after update: [[0.97409445 0.97189534]]
Episode 20 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.21557157  0.98480606 -0.24506207 -1.7060131 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0100455 1.0261664]]
Q-values after update: [[1.0207481 1.0308707]]
Designated Priority: 1
Q-values before update: [[1.0129626 1.0217496]]
Q-values after update: [[1.022999 1.026066]]
Designated Priority: 1
Q-values before update: [[1.0166522 1.017437 ]]
Q-values after update: [[1.0262018 1.021692 ]]
Designated Priority: 1
Q-values before update: [[1.0215074 1.014499 ]]
Q-values after update: [[1.0301692 1.0185841]]
Designated Priority: 1
Q-values before update: [[1.0398816 1.0297043]]
Q-values after update: [[1.0471961 1.0325081]]
Designated Priority: 1
Q-values before update: [[1.0433562 1.0260581]]
Q-values after update: [[1.0491005 1.0283839]]
Designated Priority: 1
Q-values before update: [[1.0582523 1.0389113]]
Q-values after update: [[1.061265  1.0399832]]
Designated Priority: 1
Q-values before update: [[1.0691499 1.0494924]]
Q-values after update: [[1.0692729 1.0493946]]
Designated Priority: 1
Q-values before update: [[1.0760586 1.058113 ]]
Q-values after update: [[1.0752954 1.0559999]]
Designated Priority: 1
Q-values before update: [[1.0700133 1.0482018]]
Q-values after update: [[1.0670528 1.0454375]]
Designated Priority: 1
Q-values before update: [[1.0737312 1.0540566]]
Q-values after update: [[1.0688404 1.0506066]]
Designated Priority: 1
Q-values before update: [[1.0742582 1.0581775]]
Q-values after update: [[1.0678582 1.0542204]]
Designated Priority: 1
Q-values before update: [[1.0719383 1.0602202]]
Q-values after update: [[1.0648754 1.0561004]]
Designated Priority: 1
Q-values before update: [[1.067708  1.0614283]]
Q-values after update: [[1.0611123 1.0575982]]
Designated Priority: 1
Q-values before update: [[1.063394  1.0623374]]
Q-values after update: [[1.0578744 1.0590482]]
Designated Priority: 1
Q-values before update: [[1.0585806 1.0624338]]
Q-values after update: [[1.0536036 1.0595047]]
Designated Priority: 1
Q-values before update: [[1.042926  1.0467254]]
Q-values after update: [[1.0385163 1.0440471]]
Designated Priority: 1
Q-values before update: [[1.0293732 1.0342689]]
Q-values after update: [[1.0251815 1.0313675]]
Designated Priority: 1
Q-values before update: [[1.0182549 1.0232972]]
Q-values after update: [[1.0155132 1.0211446]]
Designated Priority: 1
Q-values before update: [[1.0183847 1.0260767]]
Q-values after update: [[1.0158284 1.0239706]]
Designated Priority: 1
Q-values before update: [[1.0091858 1.0162733]]
Q-values after update: [[1.0069128 1.0143155]]
Designated Priority: 1
Q-values before update: [[1.001651  1.0071926]]
Q-values after update: [[0.9998547 1.005946 ]]
Designated Priority: 1
Q-values before update: [[0.99621284 1.0007043 ]]
Q-values after update: [[0.99527115 1.001118  ]]
Designated Priority: 1
Q-values before update: [[0.99349135 0.997812  ]]
Q-values after update: [[0.9936276 1.0002928]]
Designated Priority: 1
Q-values before update: [[0.99395645 0.998188  ]]
Q-values after update: [[0.9953975 1.0031104]]
Designated Priority: 1
Q-values before update: [[0.99715734 1.0024437 ]]
Q-values after update: [[1.0003563 1.0103694]]
Designated Priority: 1
Q-values before update: [[1.003885  1.0115232]]
Q-values after update: [[1.0091462 1.0229391]]
Designated Priority: 3
Q-values before update: [[1.0122263 1.0223362]]
Q-values after update: [[1.012528  1.0241061]]
Episode 21 out of total 100, Total Reward: 28.0, Epsilon: 0.75, Current State: [-0.00295178  1.2506338  -0.22971787 -2.5518985 ], Steps Taken: 28
Designated Priority: 1
Q-values before update: [[1.0048794 1.0231643]]
Q-values after update: [[1.0046742 1.0245965]]
Designated Priority: 1
Q-values before update: [[1.0015491 1.019573 ]]
Q-values after update: [[1.0013349 1.0207368]]
Designated Priority: 1
Q-values before update: [[0.99941987 1.0161953 ]]
Q-values after update: [[0.99930274 1.0174209 ]]
Designated Priority: 1
Q-values before update: [[0.998492  1.0138106]]
Q-values after update: [[0.9985768 1.0153917]]
Designated Priority: 1
Q-values before update: [[0.99899364 1.0130092 ]]
Q-values after update: [[0.9994528 1.0153512]]
Designated Priority: 1
Q-values before update: [[1.0018123 1.0159152]]
Q-values after update: [[1.0027245 1.0191491]]
Designated Priority: 1
Q-values before update: [[1.0058638 1.0187814]]
Q-values after update: [[1.0073649 1.023138 ]]
Designated Priority: 1
Q-values before update: [[1.0092177 1.0180051]]
Q-values after update: [[1.0118036 1.024365 ]]
Designated Priority: 1
Q-values before update: [[1.015095  1.0180683]]
Q-values after update: [[1.0194243 1.0275748]]
Designated Priority: 3
Q-values before update: [[1.0241361 1.0200819]]
Q-values after update: [[1.0190883 1.0226506]]
Episode 22 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.20790759  1.5911031  -0.2638646  -2.5390718 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.99458253 1.0391874 ]]
Q-values after update: [[0.99208915 1.0408123 ]]
Designated Priority: 1
Q-values before update: [[0.9895331 1.0368675]]
Q-values after update: [[0.9869436 1.0375187]]
Designated Priority: 1
Q-values before update: [[0.9853586 1.0343823]]
Q-values after update: [[0.9827652 1.034441 ]]
Designated Priority: 1
Q-values before update: [[0.9822226 1.0316756]]
Q-values after update: [[0.97971994 1.0314728 ]]
Designated Priority: 1
Q-values before update: [[0.9801017 1.0295566]]
Q-values after update: [[0.97778356 1.0293918 ]]
Designated Priority: 1
Q-values before update: [[0.98009396 1.030793  ]]
Q-values after update: [[0.97804093 1.0309606 ]]
Designated Priority: 1
Q-values before update: [[0.98231083 1.0336593 ]]
Q-values after update: [[0.9805232 1.034158 ]]
Designated Priority: 1
Q-values before update: [[0.9817107 1.030871 ]]
Q-values after update: [[0.9804087 1.0322123]]
Designated Priority: 1
Q-values before update: [[0.9817669 1.0274262]]
Q-values after update: [[0.9813455 1.0305021]]
Designated Priority: 1
Q-values before update: [[0.98216724 1.0207572 ]]
Q-values after update: [[0.98352337 1.0273328 ]]
Designated Priority: 3
Q-values before update: [[0.9842309 1.0174167]]
Q-values after update: [[0.9791876 1.0113367]]
Episode 23 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.17909127  2.1801114  -0.26683465 -3.316522  ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[0.98197174 1.0522758 ]]
Q-values after update: [[0.98182255 1.0520592 ]]
Designated Priority: 1
Q-values before update: [[0.9857518 1.0565479]]
Q-values after update: [[0.98514616 1.0546495 ]]
Designated Priority: 1
Q-values before update: [[0.9802812 1.0493001]]
Q-values after update: [[0.9792079 1.0461339]]
Designated Priority: 1
Q-values before update: [[0.9759164 1.0419744]]
Q-values after update: [[0.9756882 1.0393658]]
Designated Priority: 1
Q-values before update: [[0.9802426 1.044702 ]]
Q-values after update: [[0.98116386 1.0428096 ]]
Designated Priority: 1
Q-values before update: [[0.9853655 1.0475479]]
Q-values after update: [[0.9857428 1.0444295]]
Designated Priority: 1
Q-values before update: [[0.9805877 1.0388117]]
Q-values after update: [[0.98057914 1.0349442 ]]
Designated Priority: 1
Q-values before update: [[0.97699505 1.0305376 ]]
Q-values after update: [[0.976748 1.026453]]
Designated Priority: 1
Q-values before update: [[0.97417897 1.022564  ]]
Q-values after update: [[0.9738736 1.018759 ]]
Designated Priority: 1
Q-values before update: [[0.97236276 1.0158107 ]]
Q-values after update: [[0.9721657 1.0126945]]
Designated Priority: 1
Q-values before update: [[0.971923  1.0121154]]
Q-values after update: [[0.9719955 1.0100387]]
Designated Priority: 1
Q-values before update: [[0.9731102 1.0104775]]
Q-values after update: [[0.97363245 1.0097814 ]]
Designated Priority: 1
Q-values before update: [[0.97514164 1.0093881 ]]
Q-values after update: [[0.9763886 1.0105252]]
Designated Priority: 1
Q-values before update: [[0.9759173 1.0058086]]
Q-values after update: [[0.97838354 1.0096614 ]]
Designated Priority: 1
Q-values before update: [[0.9764279  0.99892104]]
Q-values after update: [[0.9812741 1.007735 ]]
Designated Priority: 3
Q-values before update: [[0.9753458 0.9896139]]
Q-values after update: [[0.9834302 1.0045868]]
Episode 24 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [ 0.14622086  1.9379853  -0.24756761 -3.075867  ], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[0.9972775 1.0399394]]
Q-values after update: [[0.9995446 1.044383 ]]
Designated Priority: 1
Q-values before update: [[1.0024889 1.0475317]]
Q-values after update: [[1.0036128 1.0493777]]
Designated Priority: 1
Q-values before update: [[1.0002915 1.0461352]]
Q-values after update: [[1.001197  1.0468445]]
Designated Priority: 1
Q-values before update: [[0.9994973 1.0451859]]
Q-values after update: [[1.0002317 1.0452654]]
Designated Priority: 1
Q-values before update: [[1.0006706 1.047208 ]]
Q-values after update: [[1.0012339 1.046663 ]]
Designated Priority: 1
Q-values before update: [[1.0030571 1.0501409]]
Q-values after update: [[1.0034186 1.049021 ]]
Designated Priority: 1
Q-values before update: [[1.0065918 1.0539997]]
Q-values after update: [[1.0066987 1.0522934]]
Designated Priority: 1
Q-values before update: [[1.0121758 1.0586976]]
Q-values after update: [[1.0119493 1.0563382]]
Designated Priority: 1
Q-values before update: [[1.0165977 1.0614853]]
Q-values after update: [[1.0176061 1.0603018]]
Designated Priority: 3
Q-values before update: [[1.0259252 1.069156 ]]
Q-values after update: [[1.0174531 1.0476515]]
Episode 25 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.1280675   1.2232785  -0.21791157 -2.0534196 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.9838214 1.0100124]]
Q-values after update: [[0.9802266  0.99750644]]
Designated Priority: 1
Q-values before update: [[0.97812265 0.99540704]]
Q-values after update: [[0.9747436 0.9843639]]
Designated Priority: 1
Q-values before update: [[0.9732933 0.9825311]]
Q-values after update: [[0.97092414 0.9726219 ]]
Designated Priority: 1
Q-values before update: [[0.9754907 0.9771738]]
Q-values after update: [[0.9739783 0.9697119]]
Designated Priority: 1
Q-values before update: [[0.97190666 0.96701896]]
Q-values after update: [[0.9712955 0.9603956]]
Designated Priority: 1
Q-values before update: [[0.9762337 0.9655365]]
Q-values after update: [[0.9763372 0.9612162]]
Designated Priority: 1
Q-values before update: [[0.97381854 0.9578563 ]]
Q-values after update: [[0.9743999  0.95558405]]
Designated Priority: 1
Q-values before update: [[0.9727031  0.95253205]]
Q-values after update: [[0.9742363 0.9507654]]
Designated Priority: 1
Q-values before update: [[0.9804288 0.9573029]]
Q-values after update: [[0.98260725 0.95608306]]
Designated Priority: 1
Q-values before update: [[0.9878973 0.9619746]]
Q-values after update: [[0.9904206 0.9611414]]
Designated Priority: 1
Q-values before update: [[0.994858   0.96604615]]
Q-values after update: [[0.9977831  0.96559143]]
Designated Priority: 1
Q-values before update: [[1.0013775 0.969761 ]]
Q-values after update: [[1.0048673  0.96971303]]
Designated Priority: 1
Q-values before update: [[1.0082395  0.97359186]]
Q-values after update: [[1.0119196  0.97505236]]
Designated Priority: 1
Q-values before update: [[1.0054328 0.968855 ]]
Q-values after update: [[1.0090895  0.97115684]]
Designated Priority: 1
Q-values before update: [[1.0040828 0.9659047]]
Q-values after update: [[1.007769  0.9680464]]
Designated Priority: 1
Q-values before update: [[1.011884 0.972777]]
Q-values after update: [[1.0159293 0.9750368]]
Designated Priority: 1
Q-values before update: [[1.0193543 0.9792432]]
Q-values after update: [[1.0237554 0.9816191]]
Designated Priority: 1
Q-values before update: [[1.0269247  0.98552716]]
Q-values after update: [[1.0318828 0.9881259]]
Designated Priority: 1
Q-values before update: [[1.034257  0.9914614]]
Q-values after update: [[1.0399649  0.99439585]]
Designated Priority: 1
Q-values before update: [[1.0401579  0.99905324]]
Q-values after update: [[1.0469313 1.0024817]]
Designated Priority: 1
Q-values before update: [[1.0378516 1.005031 ]]
Q-values after update: [[1.0465815 1.0094366]]
Designated Priority: 1
Q-values before update: [[1.0306772 1.0098097]]
Q-values after update: [[1.0426298 1.0159268]]
Designated Priority: 1
Q-values before update: [[1.0254089 1.0157075]]
Q-values after update: [[1.0421824 1.024529 ]]
Designated Priority: 3
Q-values before update: [[1.0239408 1.0238589]]
Q-values after update: [[1.0310409 1.0275466]]
Episode 26 out of total 100, Total Reward: 24.0, Epsilon: 0.75, Current State: [-0.18324879 -1.9830221   0.21793425  2.9586763 ], Steps Taken: 24
Designated Priority: 1
Q-values before update: [[1.0675302 0.9952083]]
Q-values after update: [[1.0706768 0.9966011]]
Designated Priority: 1
Q-values before update: [[1.07692   1.0032294]]
Q-values after update: [[1.0799345 1.004693 ]]
Designated Priority: 1
Q-values before update: [[1.0721799 0.9970363]]
Q-values after update: [[1.0728343 0.997518 ]]
Designated Priority: 1
Q-values before update: [[1.0794384 1.0044595]]
Q-values after update: [[1.0784812 1.0043647]]
Designated Priority: 1
Q-values before update: [[1.0848353 1.0110099]]
Q-values after update: [[1.0842326 1.0112435]]
Designated Priority: 1
Q-values before update: [[1.0746194 1.0023236]]
Q-values after update: [[1.0739719 1.002586 ]]
Designated Priority: 1
Q-values before update: [[1.066098  0.9947617]]
Q-values after update: [[1.0638552  0.99433225]]
Designated Priority: 1
Q-values before update: [[1.0709348 1.00173  ]]
Q-values after update: [[1.0677918 1.0009642]]
Designated Priority: 1
Q-values before update: [[1.0748131 1.0081514]]
Q-values after update: [[1.0710566 1.00714  ]]
Designated Priority: 1
Q-values before update: [[1.0771364 1.0136571]]
Q-values after update: [[1.0729423 1.0124311]]
Designated Priority: 1
Q-values before update: [[1.0781176 1.0184448]]
Q-values after update: [[1.0738518 1.0171373]]
Designated Priority: 1
Q-values before update: [[1.0770769 1.0237596]]
Q-values after update: [[1.0732323 1.0225719]]
Designated Priority: 1
Q-values before update: [[1.0688874 1.0284737]]
Q-values after update: [[1.0663846 1.0293422]]
Designated Priority: 1
Q-values before update: [[1.0607586 1.0159272]]
Q-values after update: [[1.0591761 1.0169423]]
Designated Priority: 1
Q-values before update: [[1.0486976 1.0199448]]
Q-values after update: [[1.0495031 1.022006 ]]
Designated Priority: 1
Q-values before update: [[1.0359156 1.0248536]]
Q-values after update: [[1.0385748 1.0302074]]
Designated Priority: 3
Q-values before update: [[1.031251  1.0156176]]
Q-values after update: [[1.0254104 1.0161542]]
Episode 27 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [-0.1684153 -1.4132932  0.2195453  2.1060598], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[1.0291402  0.98815596]]
Q-values after update: [[1.0243218 0.9885521]]
Designated Priority: 1
Q-values before update: [[1.0325031 0.9969915]]
Q-values after update: [[1.0275624 0.9971453]]
Designated Priority: 1
Q-values before update: [[1.0346557 1.0048246]]
Q-values after update: [[1.0298564 1.0048425]]
Designated Priority: 1
Q-values before update: [[1.0359024 1.0117781]]
Q-values after update: [[1.0315447 1.0117912]]
Designated Priority: 1
Q-values before update: [[1.0367515 1.0181599]]
Q-values after update: [[1.0331706 1.01837  ]]
Designated Priority: 1
Q-values before update: [[1.0280621 1.0245249]]
Q-values after update: [[1.0259602 1.0253278]]
Designated Priority: 1
Q-values before update: [[1.0129087 1.0288755]]
Q-values after update: [[1.0115547 1.0308282]]
Designated Priority: 1
Q-values before update: [[1.0060819 1.0165627]]
Q-values after update: [[1.0073801 1.0194191]]
Designated Priority: 3
Q-values before update: [[0.9939774 1.0233885]]
Q-values after update: [[0.9922651 1.0198728]]
Episode 28 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.12296425 -0.97277486  0.23206002  1.7421622 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[0.99949086 0.9884772 ]]
Q-values after update: [[0.99900544 0.98656785]]
Designated Priority: 1
Q-values before update: [[1.0068883  0.99508584]]
Q-values after update: [[1.0069052 0.9934512]]
Designated Priority: 1
Q-values before update: [[1.0137439 1.0010954]]
Q-values after update: [[1.0143528  0.99978083]]
Designated Priority: 1
Q-values before update: [[1.0202004 1.0065978]]
Q-values after update: [[1.0215468 1.0056838]]
Designated Priority: 1
Q-values before update: [[1.0264604 1.0117222]]
Q-values after update: [[1.0287503 1.0113332]]
Designated Priority: 1
Q-values before update: [[1.0229967 1.0165124]]
Q-values after update: [[1.0270444 1.0169632]]
Designated Priority: 1
Q-values before update: [[1.0138403 1.0200337]]
Q-values after update: [[1.018632  1.0225878]]
Designated Priority: 1
Q-values before update: [[1.0127068 1.0085329]]
Q-values after update: [[1.0195664 1.011999 ]]
Designated Priority: 3
Q-values before update: [[1.006369  1.0155704]]
Q-values after update: [[1.0107863 1.0147444]]
Episode 29 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.16286609 -0.9843166   0.24170908  1.7526435 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0166371  0.98469317]]
Q-values after update: [[1.0197932  0.98402745]]
Designated Priority: 1
Q-values before update: [[1.0286415 0.9929307]]
Q-values after update: [[1.031508   0.99231654]]
Designated Priority: 1
Q-values before update: [[1.0394378 1.0004584]]
Q-values after update: [[1.0419984 0.9998747]]
Designated Priority: 1
Q-values before update: [[1.0490305 1.0072773]]
Q-values after update: [[1.0513284 1.0067263]]
Designated Priority: 1
Q-values before update: [[1.0574816 1.0134073]]
Q-values after update: [[1.0596234 1.0129211]]
Designated Priority: 1
Q-values before update: [[1.0604999 1.0188847]]
Q-values after update: [[1.0630162 1.0185899]]
Designated Priority: 1
Q-values before update: [[1.0512476 1.0220705]]
Q-values after update: [[1.0551296 1.0225618]]
Designated Priority: 1
Q-values before update: [[1.0419134 1.0252011]]
Q-values after update: [[1.0486431 1.0273144]]
Designated Priority: 3
Q-values before update: [[1.0339969 1.0292126]]
Q-values after update: [[1.0286273 1.0248159]]
Episode 30 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.18472114 -1.7419211   0.25054112  2.8298528 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0404627  0.98398316]]
Q-values after update: [[1.0381008  0.98239446]]
Designated Priority: 1
Q-values before update: [[1.0470046 0.9909648]]
Q-values after update: [[1.0439205 0.9890449]]
Designated Priority: 1
Q-values before update: [[1.051553  0.9966224]]
Q-values after update: [[1.0480142 0.9944806]]
Designated Priority: 1
Q-values before update: [[1.0544226 1.0010978]]
Q-values after update: [[1.0507389 0.9988592]]
Designated Priority: 1
Q-values before update: [[1.0559665 1.0045433]]
Q-values after update: [[1.0529855 1.0036316]]
Designated Priority: 1
Q-values before update: [[1.0414602 0.9931121]]
Q-values after update: [[1.0391484  0.99248606]]
Designated Priority: 1
Q-values before update: [[1.044242   0.99801666]]
Q-values after update: [[1.0425764 0.9975855]]
Designated Priority: 1
Q-values before update: [[1.041033 1.001035]]
Q-values after update: [[1.0405416 1.0010722]]
Designated Priority: 1
Q-values before update: [[1.026402  1.0025474]]
Q-values after update: [[1.0286393 1.0038664]]
Designated Priority: 1
Q-values before update: [[1.0128939 1.004412 ]]
Q-values after update: [[1.019687  1.0081027]]
Designated Priority: 3
Q-values before update: [[1.0024484 1.0078597]]
Q-values after update: [[1.0075102 1.0088977]]
Episode 31 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.19573463 -1.3331153   0.25475302  2.2464418 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0320356  0.97855693]]
Q-values after update: [[1.0340836  0.97851455]]
Designated Priority: 1
Q-values before update: [[1.0424984  0.98653805]]
Q-values after update: [[1.0437106  0.98629045]]
Designated Priority: 1
Q-values before update: [[1.0512215 0.9936025]]
Q-values after update: [[1.0516737  0.99315155]]
Designated Priority: 1
Q-values before update: [[1.0582849 0.9997542]]
Q-values after update: [[1.0581002  0.99911565]]
Designated Priority: 1
Q-values before update: [[1.0638871 1.0050445]]
Q-values after update: [[1.0632461 1.0042615]]
Designated Priority: 1
Q-values before update: [[1.0645219 1.0089948]]
Q-values after update: [[1.0640184 1.0082204]]
Designated Priority: 1
Q-values before update: [[1.051407  1.0102082]]
Q-values after update: [[1.0520675 1.0100235]]
Designated Priority: 1
Q-values before update: [[1.0377622 1.0111254]]
Q-values after update: [[1.041206  1.0124234]]
Designated Priority: 3
Q-values before update: [[1.0253367 1.0126085]]
Q-values after update: [[1.0200706 1.0091944]]
Episode 32 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.15386753 -1.7172552   0.2416099   2.8505702 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0343071 0.9753459]]
Q-values after update: [[1.0310354  0.97383296]]
Designated Priority: 1
Q-values before update: [[1.0395466  0.98179865]]
Q-values after update: [[1.0357394  0.98002356]]
Designated Priority: 1
Q-values before update: [[1.0430312  0.98704576]]
Q-values after update: [[1.0389649  0.98511744]]
Designated Priority: 1
Q-values before update: [[1.0450842  0.99122417]]
Q-values after update: [[1.0410725  0.98926824]]
Designated Priority: 1
Q-values before update: [[1.0460638 0.9944844]]
Q-values after update: [[1.0424688 0.9926618]]
Designated Priority: 1
Q-values before update: [[1.0460291  0.99724764]]
Q-values after update: [[1.0432206 0.9957402]]
Designated Priority: 1
Q-values before update: [[1.0295706 0.9965811]]
Q-values after update: [[1.0289979  0.99611425]]
Designated Priority: 1
Q-values before update: [[1.0134217 0.9959282]]
Q-values after update: [[1.0168338  0.99749565]]
Designated Priority: 3
Q-values before update: [[0.999628  0.9963534]]
Q-values after update: [[1.003064  0.9979894]]
Episode 33 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.14084005 -1.7186916   0.22012584  2.783789  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0216477 0.9707582]]
Q-values after update: [[1.0226169 0.9709771]]
Designated Priority: 1
Q-values before update: [[1.030554  0.9784774]]
Q-values after update: [[1.0312428 0.9786617]]
Designated Priority: 1
Q-values before update: [[1.0383167 0.9855069]]
Q-values after update: [[1.0393679 0.9866148]]
Designated Priority: 1
Q-values before update: [[1.0289474 0.9771952]]
Q-values after update: [[1.0295222  0.97799325]]
Designated Priority: 1
Q-values before update: [[1.0369804 0.9851431]]
Q-values after update: [[1.0374336  0.98588943]]
Designated Priority: 1
Q-values before update: [[1.0440208 0.9923782]]
Q-values after update: [[1.0444763 0.9931135]]
Designated Priority: 1
Q-values before update: [[1.0502145 0.9989491]]
Q-values after update: [[1.0508423  0.99974334]]
Designated Priority: 1
Q-values before update: [[1.055549 1.005202]]
Q-values after update: [[1.0566101 1.0061388]]
Designated Priority: 1
Q-values before update: [[1.0464058 1.0086756]]
Q-values after update: [[1.0490966 1.0103859]]
Designated Priority: 1
Q-values before update: [[1.0354323 1.0115083]]
Q-values after update: [[1.0410811 1.0147495]]
Designated Priority: 3
Q-values before update: [[1.0259731 1.0150642]]
Q-values after update: [[1.0286782 1.0133681]]
Episode 34 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.14677136 -1.3605891   0.22149561  2.2236593 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.023561   0.96906716]]
Q-values after update: [[1.0248482 0.9678035]]
Designated Priority: 1
Q-values before update: [[1.0345428 0.9765769]]
Q-values after update: [[1.0354066 0.975285 ]]
Designated Priority: 1
Q-values before update: [[1.0440924  0.98322225]]
Q-values after update: [[1.0445626  0.98189825]]
Designated Priority: 1
Q-values before update: [[1.0522624 0.9890194]]
Q-values after update: [[1.0524108  0.98767394]]
Designated Priority: 1
Q-values before update: [[1.0591431  0.99399257]]
Q-values after update: [[1.0591102 0.9926683]]
Designated Priority: 1
Q-values before update: [[1.0611019  0.99675363]]
Q-values after update: [[1.0614395 0.995613 ]]
Designated Priority: 1
Q-values before update: [[1.0504236  0.99693304]]
Q-values after update: [[1.0522135  0.99654275]]
Designated Priority: 3
Q-values before update: [[1.0389612 0.9974402]]
Q-values after update: [[1.0289297 0.9909366]]
Episode 35 out of total 100, Total Reward: 8.0, Epsilon: 0.75, Current State: [-0.11839491 -1.6165385   0.22305876  2.5484538 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[1.0237597  0.95810145]]
Q-values after update: [[1.0184634  0.95542204]]
Designated Priority: 1
Q-values before update: [[1.027523  0.9633037]]
Q-values after update: [[1.0218782  0.96037483]]
Designated Priority: 1
Q-values before update: [[1.0296116 0.9673099]]
Q-values after update: [[1.023909   0.96426654]]
Designated Priority: 1
Q-values before update: [[1.0303657 0.970147 ]]
Q-values after update: [[1.0249603 0.967147 ]]
Designated Priority: 1
Q-values before update: [[1.0301634  0.97211814]]
Q-values after update: [[1.0254567  0.96935904]]
Designated Priority: 1
Q-values before update: [[1.0236442  0.96978253]]
Q-values after update: [[1.0200814 0.9695923]]
Designated Priority: 1
Q-values before update: [[1.0137571  0.96206176]]
Q-values after update: [[1.0119158  0.96244097]]
Designated Priority: 1
Q-values before update: [[1.0014441 0.9586001]]
Q-values after update: [[1.001859   0.95990956]]
Designated Priority: 3
Q-values before update: [[0.9863294 0.9589286]]
Q-values after update: [[0.990121  0.9618188]]
Episode 36 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.07352837 -1.3720309   0.23251957  2.2780128 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0027832 0.957481 ]]
Q-values after update: [[1.0054177  0.95925736]]
Designated Priority: 1
Q-values before update: [[1.0126067  0.96575797]]
Q-values after update: [[1.0157844  0.96773136]]
Designated Priority: 1
Q-values before update: [[1.0221243 0.9735886]]
Q-values after update: [[1.0258734 0.9757774]]
Designated Priority: 1
Q-values before update: [[1.0314    0.9810097]]
Q-values after update: [[1.0357889 0.9834607]]
Designated Priority: 1
Q-values before update: [[1.040543  0.9880912]]
Q-values after update: [[1.045683   0.99088335]]
Designated Priority: 1
Q-values before update: [[1.0497117 0.9949408]]
Q-values after update: [[1.0557535 0.9981865]]
Designated Priority: 1
Q-values before update: [[1.0482594 1.0003797]]
Q-values after update: [[1.0562861 1.0046606]]
Designated Priority: 1
Q-values before update: [[1.0418414 1.0036665]]
Q-values after update: [[1.0530704 1.0096648]]
Designated Priority: 1
Q-values before update: [[1.0369561 1.008302 ]]
Q-values after update: [[1.0531651 1.0171367]]
Designated Priority: 3
Q-values before update: [[1.0363125 1.0154463]]
Q-values after update: [[1.0370306 1.0155878]]
Episode 37 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.22521025 -1.9976916   0.25524372  3.113565  ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0488833 0.9773853]]
Q-values after update: [[1.0495697 0.9778812]]
Designated Priority: 1
Q-values before update: [[1.0594021 0.9864726]]
Q-values after update: [[1.0601684 0.9873753]]
Designated Priority: 1
Q-values before update: [[1.0492374  0.97792524]]
Q-values after update: [[1.050306   0.97975874]]
Designated Priority: 1
Q-values before update: [[1.0406761 0.9713254]]
Q-values after update: [[1.0403509  0.97249687]]
Designated Priority: 1
Q-values before update: [[1.0510753  0.98173106]]
Q-values after update: [[1.0494802  0.98230976]]
Designated Priority: 1
Q-values before update: [[1.0591621  0.99082315]]
Q-values after update: [[1.0564024 0.9908402]]
Designated Priority: 1
Q-values before update: [[1.0650485  0.99864495]]
Q-values after update: [[1.061315   0.99814576]]
Designated Priority: 1
Q-values before update: [[1.0688062 1.0050454]]
Q-values after update: [[1.0643642 1.0041156]]
Designated Priority: 1
Q-values before update: [[1.0706785 1.010131 ]]
Q-values after update: [[1.0669758 1.010118 ]]
Designated Priority: 1
Q-values before update: [[1.0532408 0.9980323]]
Q-values after update: [[1.0495889 0.9978693]]
Designated Priority: 1
Q-values before update: [[1.0559704 1.0038462]]
Q-values after update: [[1.052503  1.0036083]]
Designated Priority: 1
Q-values before update: [[1.0504265 1.0051453]]
Q-values after update: [[1.0478613 1.0051994]]
Designated Priority: 1
Q-values before update: [[1.0341552 1.0054581]]
Q-values after update: [[1.0340681 1.0066326]]
Designated Priority: 3
Q-values before update: [[1.0184178 1.0058084]]
Q-values after update: [[1.0127394 1.0038772]]
Episode 38 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [-0.12892953 -1.6018625   0.23624429  2.6030219 ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[1.0235993 0.9841516]]
Q-values after update: [[1.0202231 0.9836433]]
Designated Priority: 1
Q-values before update: [[1.0288984  0.99159306]]
Q-values after update: [[1.0258206 0.9913573]]
Designated Priority: 1
Q-values before update: [[1.0161116 0.9826894]]
Q-values after update: [[1.0138147 0.983504 ]]
Designated Priority: 1
Q-values before update: [[1.005592 0.975701]]
Q-values after update: [[1.0035204  0.97646856]]
Designated Priority: 1
Q-values before update: [[1.0126643 0.9851363]]
Q-values after update: [[1.010927  0.9858469]]
Designated Priority: 1
Q-values before update: [[1.019104   0.99347806]]
Q-values after update: [[1.0178474 0.9942044]]
Designated Priority: 1
Q-values before update: [[1.0248917 1.0009419]]
Q-values after update: [[1.0242503 1.001761 ]]
Designated Priority: 1
Q-values before update: [[1.0302212 1.0076387]]
Q-values after update: [[1.0303967 1.0086665]]
Designated Priority: 1
Q-values before update: [[1.0354316 1.0138389]]
Q-values after update: [[1.0360726 1.0159926]]
Designated Priority: 1
Q-values before update: [[1.0239593 1.0051761]]
Q-values after update: [[1.0256076 1.0075163]]
Designated Priority: 1
Q-values before update: [[1.030832  1.0127728]]
Q-values after update: [[1.0336862 1.0155189]]
Designated Priority: 1
Q-values before update: [[1.0380018 1.0200326]]
Q-values after update: [[1.0422668 1.0233579]]
Designated Priority: 1
Q-values before update: [[1.0331349 1.0244551]]
Q-values after update: [[1.0398539 1.0289679]]
Designated Priority: 1
Q-values before update: [[1.0240688 1.0272701]]
Q-values after update: [[1.0349555 1.0339856]]
Designated Priority: 3
Q-values before update: [[1.0172889 1.0318086]]
Q-values after update: [[1.0215125 1.0274565]]
Episode 39 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [-0.18321905 -1.3933101   0.21664019  2.1322868 ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[1.0326017 0.9986908]]
Q-values after update: [[1.0355861 0.9963204]]
Designated Priority: 1
Q-values before update: [[1.0448121 1.0045514]]
Q-values after update: [[1.0475177 1.0023105]]
Designated Priority: 1
Q-values before update: [[1.0374589  0.99351037]]
Q-values after update: [[1.0388047 0.991182 ]]
Designated Priority: 1
Q-values before update: [[1.0480692  0.99920386]]
Q-values after update: [[1.0481708  0.99659514]]
Designated Priority: 1
Q-values before update: [[1.0564764 1.0038836]]
Q-values after update: [[1.0554556 1.0009984]]
Designated Priority: 1
Q-values before update: [[1.0626037 1.0072587]]
Q-values after update: [[1.061754  1.0048472]]
Designated Priority: 1
Q-values before update: [[1.049433   0.99438214]]
Q-values after update: [[1.0478866  0.99197805]]
Designated Priority: 1
Q-values before update: [[1.055063 0.998068]]
Q-values after update: [[1.0529339 0.99552  ]]
Designated Priority: 1
Q-values before update: [[1.0589314 1.0005772]]
Q-values after update: [[1.0564777 0.9979725]]
Designated Priority: 1
Q-values before update: [[1.0584772 1.0001553]]
Q-values after update: [[1.0561342  0.99767184]]
Designated Priority: 1
Q-values before update: [[1.0428905  0.99321246]]
Q-values after update: [[1.0421724 0.9914826]]
Designated Priority: 1
Q-values before update: [[1.0251275 0.9876176]]
Q-values after update: [[1.0277743 0.9877049]]
Designated Priority: 3
Q-values before update: [[1.0091083 0.982898 ]]
Q-values after update: [[1.0085747  0.98131686]]
Episode 40 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.1292848  -1.7369756   0.25535437  2.8426375 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0323981  0.97728777]]
Q-values after update: [[1.0314186 0.9761356]]
Designated Priority: 1
Q-values before update: [[1.0399277 0.9829892]]
Q-values after update: [[1.0386806  0.98178184]]
Designated Priority: 1
Q-values before update: [[1.046099  0.9877539]]
Q-values after update: [[1.0453963 0.9877996]]
Designated Priority: 1
Q-values before update: [[1.0345474 0.9792719]]
Q-values after update: [[1.0337948 0.9792733]]
Designated Priority: 1
Q-values before update: [[1.0413655 0.9853196]]
Q-values after update: [[1.0406972 0.9853163]]
Designated Priority: 1
Q-values before update: [[1.0472184  0.99051416]]
Q-values after update: [[1.0468196 0.9905869]]
Designated Priority: 1
Q-values before update: [[1.0524263  0.99509776]]
Q-values after update: [[1.0525198 0.9953558]]
Designated Priority: 1
Q-values before update: [[1.0572754 0.9992329]]
Q-values after update: [[1.0581454  0.99983865]]
Designated Priority: 1
Q-values before update: [[1.0553952 1.000098 ]]
Q-values after update: [[1.0579135 1.0014954]]
Designated Priority: 1
Q-values before update: [[1.0427814  0.99697244]]
Q-values after update: [[1.048493  1.0000949]]
Designated Priority: 1
Q-values before update: [[1.0312104  0.99486816]]
Q-values after update: [[1.0420781 1.0007849]]
Designated Priority: 3
Q-values before update: [[1.0231936  0.99536955]]
Q-values after update: [[1.0244985  0.99589515]]
Episode 41 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.20967643 -1.9581225   0.24426018  3.0317328 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.029656  0.9711137]]
Q-values after update: [[1.0301864 0.9713907]]
Designated Priority: 1
Q-values before update: [[1.0400686 0.9790504]]
Q-values after update: [[1.0400071  0.97909474]]
Designated Priority: 1
Q-values before update: [[1.048761   0.98584867]]
Q-values after update: [[1.0481982 0.9857173]]
Designated Priority: 1
Q-values before update: [[1.0561244 0.9919902]]
Q-values after update: [[1.0551411 0.9916635]]
Designated Priority: 1
Q-values before update: [[1.0619411 0.9969888]]
Q-values after update: [[1.0607234 0.9965304]]
Designated Priority: 1
Q-values before update: [[1.0631747 0.9987288]]
Q-values after update: [[1.0621946  0.99836385]]
Designated Priority: 1
Q-values before update: [[1.0499886  0.99334264]]
Q-values after update: [[1.0506073  0.99376225]]
Designated Priority: 3
Q-values before update: [[1.0343508  0.98981434]]
Q-values after update: [[1.0242382 0.9844012]]
Episode 42 out of total 100, Total Reward: 8.0, Epsilon: 0.75, Current State: [-0.13808963 -1.5737294   0.22004065  2.5642626 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[1.0247271 0.9703367]]
Q-values after update: [[1.0193026  0.96836007]]
Designated Priority: 1
Q-values before update: [[1.0285372  0.97561157]]
Q-values after update: [[1.0228798  0.97339666]]
Designated Priority: 1
Q-values before update: [[1.0307592 0.9796637]]
Q-values after update: [[1.025171  0.9773271]]
Designated Priority: 1
Q-values before update: [[1.0315803 0.982371 ]]
Q-values after update: [[1.0267503 0.981246 ]]
Designated Priority: 1
Q-values before update: [[1.0154483  0.97195333]]
Q-values after update: [[1.0116659 0.9712375]]
Designated Priority: 1
Q-values before update: [[1.0176338 0.9758562]]
Q-values after update: [[1.014652  0.9753058]]
Designated Priority: 1
Q-values before update: [[1.019289  0.9787923]]
Q-values after update: [[1.0172575 0.9800958]]
Designated Priority: 1
Q-values before update: [[1.0053841 0.9701002]]
Q-values after update: [[1.0047631 0.9717819]]
Designated Priority: 1
Q-values before update: [[1.0092908  0.97511894]]
Q-values after update: [[1.0100049 0.9771836]]
Designated Priority: 1
Q-values before update: [[0.99750376 0.96906626]]
Q-values after update: [[0.9997734  0.97419804]]
Designated Priority: 3
Q-values before update: [[0.9925468 0.966753 ]]
Q-values after update: [[0.99796325 0.9783261 ]]
Episode 43 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.10419533 -0.5650788   0.21850762  1.147026  ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0065463 0.9879904]]
Q-values after update: [[1.0099375  0.99654686]]
Designated Priority: 1
Q-values before update: [[1.0183035 1.0038431]]
Q-values after update: [[1.0216161 1.0118308]]
Designated Priority: 1
Q-values before update: [[1.0118434 1.0033407]]
Q-values after update: [[1.0149003 1.0103643]]
Designated Priority: 1
Q-values before update: [[1.0238414 1.0183885]]
Q-values after update: [[1.0271437 1.0251703]]
Designated Priority: 1
Q-values before update: [[1.0351961 1.0325396]]
Q-values after update: [[1.0382385 1.0385494]]
Designated Priority: 1
Q-values before update: [[1.0267563 1.0282496]]
Q-values after update: [[1.028927  1.0323523]]
Designated Priority: 1
Q-values before update: [[1.0184699 1.0228407]]
Q-values after update: [[1.0201061 1.025884 ]]
Designated Priority: 1
Q-values before update: [[1.0107787 1.0172179]]
Q-values after update: [[1.0120827 1.0197362]]
Designated Priority: 1
Q-values before update: [[1.0043571 1.0113847]]
Q-values after update: [[1.0055053 1.0138133]]
Designated Priority: 1
Q-values before update: [[0.9990995 1.0067635]]
Q-values after update: [[1.0003747 1.0096685]]
Designated Priority: 1
Q-values before update: [[0.99635446 1.0039529 ]]
Q-values after update: [[0.9984    1.0069289]]
Designated Priority: 1
Q-values before update: [[1.0099256 1.0188854]]
Q-values after update: [[1.0119734 1.022028 ]]
Designated Priority: 1
Q-values before update: [[1.0074486 1.0153852]]
Q-values after update: [[1.0096276 1.0190002]]
Designated Priority: 1
Q-values before update: [[1.006278  1.0132105]]
Q-values after update: [[1.0088676 1.0178008]]
Designated Priority: 1
Q-values before update: [[1.0060632 1.0138881]]
Q-values after update: [[1.0092927 1.0198336]]
Designated Priority: 3
Q-values before update: [[1.0050387 1.0135882]]
Q-values after update: [[1.0066609 1.0182123]]
Episode 44 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [ 0.08295035  1.1758829  -0.22918607 -2.0394084 ], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[1.0441604 1.0634046]]
Q-values after update: [[1.0446535 1.0649818]]
Designated Priority: 1
Q-values before update: [[1.0347315 1.0556259]]
Q-values after update: [[1.0345466 1.0553055]]
Designated Priority: 1
Q-values before update: [[1.0263233 1.0463715]]
Q-values after update: [[1.0257245 1.0449338]]
Designated Priority: 1
Q-values before update: [[1.0190557 1.0374746]]
Q-values after update: [[1.0183203 1.0356656]]
Designated Priority: 1
Q-values before update: [[1.0134174 1.0292959]]
Q-values after update: [[1.0127265 1.0276439]]
Designated Priority: 1
Q-values before update: [[1.0100129 1.0226893]]
Q-values after update: [[1.0096722 1.0218331]]
Designated Priority: 1
Q-values before update: [[1.0081974 1.0184667]]
Q-values after update: [[1.0084949 1.0190079]]
Designated Priority: 1
Q-values before update: [[1.0041963 1.0128276]]
Q-values after update: [[1.0057168 1.0156893]]
Designated Priority: 3
Q-values before update: [[1.0005032 1.006805 ]]
Q-values after update: [[1.0005571 1.0069382]]
Episode 45 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [ 0.13402183  1.8126069  -0.2559772  -2.8933089 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0455574 1.0615268]]
Q-values after update: [[1.0446712 1.0591731]]
Designated Priority: 1
Q-values before update: [[1.0348016 1.0500522]]
Q-values after update: [[1.0334679 1.0464642]]
Designated Priority: 1
Q-values before update: [[1.025274  1.0378747]]
Q-values after update: [[1.0238955 1.0340283]]
Designated Priority: 1
Q-values before update: [[1.0174508 1.0271013]]
Q-values after update: [[1.0161347 1.0234947]]
Designated Priority: 1
Q-values before update: [[1.0108519 1.0174079]]
Q-values after update: [[1.0098748 1.0146742]]
Designated Priority: 1
Q-values before update: [[1.0069895 1.0096955]]
Q-values after update: [[1.0066892 1.0084893]]
Designated Priority: 1
Q-values before update: [[1.0052713 1.0056975]]
Q-values after update: [[1.0059521 1.0065868]]
Designated Priority: 1
Q-values before update: [[1.0015011 1.0004171]]
Q-values after update: [[1.0040784 1.0024858]]
Designated Priority: 3
Q-values before update: [[1.017702  1.0162153]]
Q-values after update: [[1.0152221 1.0151085]]
Episode 46 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [ 0.15332869  1.0349609  -0.2417461  -1.7107989 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.028887  1.0361974]]
Q-values after update: [[1.0267415 1.0342941]]
Designated Priority: 1
Q-values before update: [[1.0181823 1.0266877]]
Q-values after update: [[1.0160322 1.0244362]]
Designated Priority: 1
Q-values before update: [[1.0089668 1.0177134]]
Q-values after update: [[1.0070124 1.0156965]]
Designated Priority: 1
Q-values before update: [[1.0009325 1.0094178]]
Q-values after update: [[0.99935853 1.0081179 ]]
Designated Priority: 1
Q-values before update: [[0.9961758 1.0043657]]
Q-values after update: [[0.9952143 1.0042613]]
Designated Priority: 1
Q-values before update: [[0.99345714 1.0010239 ]]
Q-values after update: [[0.9932877 1.0024787]]
Designated Priority: 1
Q-values before update: [[0.9921669 1.0003998]]
Q-values after update: [[0.9930259 1.0038751]]
Designated Priority: 1
Q-values before update: [[0.99005485 0.99979746]]
Q-values after update: [[0.99238575 1.0059428 ]]
Designated Priority: 3
Q-values before update: [[0.9877231  0.99846935]]
Q-values after update: [[0.99036735 1.0049219 ]]
Episode 47 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [ 0.0950929   1.7738895  -0.21986473 -2.8069046 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0165331 1.034056 ]]
Q-values after update: [[1.0171198 1.037207 ]]
Designated Priority: 1
Q-values before update: [[1.0258592 1.0446346]]
Q-values after update: [[1.025718  1.0459117]]
Designated Priority: 1
Q-values before update: [[1.0163615 1.0378349]]
Q-values after update: [[1.0160704 1.0382185]]
Designated Priority: 1
Q-values before update: [[1.0088058 1.032196 ]]
Q-values after update: [[1.0087404 1.0327885]]
Designated Priority: 1
Q-values before update: [[1.0170212 1.0393784]]
Q-values after update: [[1.0164039 1.0386058]]
Designated Priority: 1
Q-values before update: [[1.0092647 1.0328367]]
Q-values after update: [[1.008574  1.0314902]]
Designated Priority: 1
Q-values before update: [[1.0029346 1.0269437]]
Q-values after update: [[1.0022979 1.0255482]]
Designated Priority: 1
Q-values before update: [[0.9989799 1.0235612]]
Q-values after update: [[0.9985379 1.0225123]]
Designated Priority: 1
Q-values before update: [[0.9964762 1.021282 ]]
Q-values after update: [[0.9962986 1.0207953]]
Designated Priority: 1
Q-values before update: [[0.995485  1.0201715]]
Q-values after update: [[0.9956837 1.0204875]]
Designated Priority: 1
Q-values before update: [[0.996433  1.0206043]]
Q-values after update: [[0.9971129 1.0219758]]
Designated Priority: 1
Q-values before update: [[0.9985421 1.02356  ]]
Q-values after update: [[0.9998058 1.0260935]]
Designated Priority: 1
Q-values before update: [[0.99991834 1.0253861 ]]
Q-values after update: [[1.0020851 1.0295852]]
Designated Priority: 1
Q-values before update: [[1.0000418 1.0248492]]
Q-values after update: [[1.0035344 1.0314044]]
Designated Priority: 3
Q-values before update: [[1.0005435 1.023851 ]]
Q-values after update: [[0.9972651 1.0180228]]
Episode 48 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [ 0.16129164  2.095037   -0.24073298 -3.1936734 ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[1.020057  1.0416158]]
Q-values after update: [[1.0189165 1.03869  ]]
Designated Priority: 1
Q-values before update: [[1.0131763 1.0346614]]
Q-values after update: [[1.0118101 1.0312132]]
Designated Priority: 1
Q-values before update: [[1.007169  1.0278847]]
Q-values after update: [[1.0057576 1.0244315]]
Designated Priority: 1
Q-values before update: [[1.0020425 1.0214907]]
Q-values after update: [[1.0007733 1.0185137]]
Designated Priority: 1
Q-values before update: [[0.99901974 1.0177126 ]]
Q-values after update: [[0.99808407 1.0156133 ]]
Designated Priority: 1
Q-values before update: [[0.9981016 1.0162256]]
Q-values after update: [[0.99766   1.0152856]]
Designated Priority: 1
Q-values before update: [[0.99791765 1.0162898 ]]
Q-values after update: [[0.9981661 1.0168781]]
Designated Priority: 1
Q-values before update: [[0.99616957 1.014345  ]]
Q-values after update: [[0.9974693 1.0170153]]
Designated Priority: 1
Q-values before update: [[0.9923866 1.0069643]]
Q-values after update: [[0.99567616 1.0132535 ]]
Designated Priority: 3
Q-values before update: [[0.9917685 1.0031583]]
Q-values after update: [[0.99424267 1.0076991 ]]
Episode 49 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.18174346  1.9524918  -0.25723228 -3.1074843 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0207036 1.0358536]]
Q-values after update: [[1.0210115 1.0369256]]
Designated Priority: 1
Q-values before update: [[1.0152093 1.0329684]]
Q-values after update: [[1.0151644 1.0339599]]
Designated Priority: 1
Q-values before update: [[1.0218544 1.0385382]]
Q-values after update: [[1.0212446 1.0380867]]
Designated Priority: 1
Q-values before update: [[1.0157019 1.0344726]]
Q-values after update: [[1.0150826 1.033586 ]]
Designated Priority: 1
Q-values before update: [[1.0110694 1.0311766]]
Q-values after update: [[1.0104537 1.0301166]]
Designated Priority: 1
Q-values before update: [[1.0075738 1.0283145]]
Q-values after update: [[1.0070691 1.027405 ]]
Designated Priority: 1
Q-values before update: [[1.005749  1.0272024]]
Q-values after update: [[1.0054755 1.0267332]]
Designated Priority: 1
Q-values before update: [[1.0060169 1.0290525]]
Q-values after update: [[1.0060244 1.029186 ]]
Designated Priority: 1
Q-values before update: [[1.0078052 1.0321053]]
Q-values after update: [[1.008209 1.033009]]
Designated Priority: 1
Q-values before update: [[1.0065618 1.0310333]]
Q-values after update: [[1.0077848 1.0334435]]
Designated Priority: 3
Q-values before update: [[1.004057  1.0251863]]
Q-values after update: [[0.9995501 1.0166191]]
Episode 50 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.1997739   1.7990664  -0.21130715 -2.7471418 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0081774 1.0268632]]
Q-values after update: [[1.0066562 1.0228593]]
Designated Priority: 1
Q-values before update: [[1.0019199 1.0200465]]
Q-values after update: [[1.000361  1.0161589]]
Designated Priority: 1
Q-values before update: [[0.99643004 1.013959  ]]
Q-values after update: [[0.99500656 1.0106158 ]]
Designated Priority: 1
Q-values before update: [[0.99276817 1.0097368 ]]
Q-values after update: [[0.99165267 1.0073029 ]]
Designated Priority: 1
Q-values before update: [[0.99109274 1.0077561 ]]
Q-values after update: [[0.99043894 1.0064586 ]]
Designated Priority: 1
Q-values before update: [[0.99110395 1.0077654 ]]
Q-values after update: [[0.99105775 1.0079123 ]]
Designated Priority: 1
Q-values before update: [[0.9920865 1.0095979]]
Q-values after update: [[0.9928549 1.0114713]]
Designated Priority: 1
Q-values before update: [[0.990007  1.0052638]]
Q-values after update: [[0.9920132 1.0094845]]
Designated Priority: 1
Q-values before update: [[0.9864689 0.9977448]]
Q-values after update: [[0.9909886 1.0065176]]
Designated Priority: 3
Q-values before update: [[0.986088  0.9952576]]
Q-values after update: [[0.9918035 1.0059803]]
Episode 51 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.13297854  1.9167432  -0.24967717 -3.1086285 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0129923 1.0293264]]
Q-values after update: [[1.0144008 1.0333753]]
Designated Priority: 1
Q-values before update: [[1.0101389 1.0311644]]
Q-values after update: [[1.0114526 1.0345604]]
Designated Priority: 1
Q-values before update: [[1.0084039 1.0334607]]
Q-values after update: [[1.0096363 1.0363655]]
Designated Priority: 1
Q-values before update: [[1.0078529 1.0359697]]
Q-values after update: [[1.0090204 1.0384905]]
Designated Priority: 1
Q-values before update: [[1.0095469 1.0408946]]
Q-values after update: [[1.0112015 1.043654 ]]
Designated Priority: 1
Q-values before update: [[1.0174149 1.046623 ]]
Q-values after update: [[1.0184101 1.0479965]]
Designated Priority: 1
Q-values before update: [[1.0178967 1.0497739]]
Q-values after update: [[1.0186018 1.0504405]]
Designated Priority: 1
Q-values before update: [[1.0207946 1.0545311]]
Q-values after update: [[1.0212302 1.0545523]]
Designated Priority: 1
Q-values before update: [[1.0245193 1.059631 ]]
Q-values after update: [[1.0246465 1.0589823]]
Designated Priority: 1
Q-values before update: [[1.0230827 1.0554613]]
Q-values after update: [[1.0233486 1.0551187]]
Designated Priority: 3
Q-values before update: [[1.0208857 1.0475734]]
Q-values after update: [[1.0095098 1.0256717]]
Episode 52 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.2109691   1.7920394  -0.24978249 -2.8375936 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0154345 1.0350051]]
Q-values after update: [[1.0118964 1.0248357]]
Designated Priority: 1
Q-values before update: [[1.0075991 1.0227292]]
Q-values after update: [[1.0037858 1.0125872]]
Designated Priority: 1
Q-values before update: [[0.9999658 1.0106573]]
Q-values after update: [[0.99618006 1.0012324 ]]
Designated Priority: 1
Q-values before update: [[0.9937998 1.0005141]]
Q-values after update: [[0.9903401 0.992377 ]]
Designated Priority: 1
Q-values before update: [[0.9896486 0.9921004]]
Q-values after update: [[0.9867769 0.9857681]]
Designated Priority: 1
Q-values before update: [[0.98700684 0.98545325]]
Q-values after update: [[0.98548377 0.9800705 ]]
Designated Priority: 1
Q-values before update: [[0.9915569 0.9839639]]
Q-values after update: [[0.9912276  0.97971857]]
Designated Priority: 1
Q-values before update: [[0.9994239 0.9868885]]
Q-values after update: [[0.9996713 0.9833835]]
Designated Priority: 1
Q-values before update: [[1.0082943 0.9903461]]
Q-values after update: [[1.0085098  0.98726934]]
Designated Priority: 1
Q-values before update: [[1.0163714 0.9937829]]
Q-values after update: [[1.0160998 0.990903 ]]
Designated Priority: 1
Q-values before update: [[1.0232333  0.99699056]]
Q-values after update: [[1.0229173  0.99444294]]
Designated Priority: 1
Q-values before update: [[1.0294448 1.001321 ]]
Q-values after update: [[1.0286571 0.9988988]]
Designated Priority: 1
Q-values before update: [[1.0349282 1.0060256]]
Q-values after update: [[1.0342121 1.0039029]]
Designated Priority: 1
Q-values before update: [[1.0399116 1.0107412]]
Q-values after update: [[1.0397878 1.0090946]]
Designated Priority: 1
Q-values before update: [[1.0449355 1.0151858]]
Q-values after update: [[1.0460938 1.0142863]]
Designated Priority: 1
Q-values before update: [[1.0493538 1.0186875]]
Q-values after update: [[1.0531313 1.0193223]]
Designated Priority: 1
Q-values before update: [[1.0553879 1.0224776]]
Q-values after update: [[1.0627434 1.0252427]]
Designated Priority: 1
Q-values before update: [[1.0639799 1.0295422]]
Q-values after update: [[1.0727586 1.0363292]]
Designated Priority: 1
Q-values before update: [[1.0594813 1.021679 ]]
Q-values after update: [[1.0682169 1.0300282]]
Designated Priority: 1
Q-values before update: [[1.054121  1.0175703]]
Q-values after update: [[1.0639617 1.025749 ]]
Designated Priority: 1
Q-values before update: [[1.0704485 1.0322313]]
Q-values after update: [[1.0828482 1.0415523]]
Designated Priority: 1
Q-values before update: [[1.0885578 1.0482306]]
Q-values after update: [[1.1009035 1.0602927]]
Designated Priority: 1
Q-values before update: [[1.0863023 1.0451386]]
Q-values after update: [[1.0988576 1.056161 ]]
Designated Priority: 1
Q-values before update: [[1.1060312 1.0640821]]
Q-values after update: [[1.1200166 1.0757209]]
Designated Priority: 1
Q-values before update: [[1.1247063 1.0862876]]
Q-values after update: [[1.1403205 1.0986747]]
Designated Priority: 1
Q-values before update: [[1.1375194 1.1039438]]
Q-values after update: [[1.1555573 1.1176591]]
Designated Priority: 1
Q-values before update: [[1.1444281 1.1171166]]
Q-values after update: [[1.1664057 1.1330595]]
Designated Priority: 1
Q-values before update: [[1.1541868 1.1316476]]
Q-values after update: [[1.1817758 1.1509569]]
Designated Priority: 3
Q-values before update: [[1.1687728 1.149552 ]]
Q-values after update: [[1.087892  1.1024587]]
Episode 53 out of total 100, Total Reward: 29.0, Epsilon: 0.75, Current State: [-0.37085542 -2.4787743   0.25470078  3.1818216 ], Steps Taken: 29
Designated Priority: 1
Q-values before update: [[1.0756414 1.0289928]]
Q-values after update: [[1.0535007 1.0216429]]
Designated Priority: 1
Q-values before update: [[1.0630941 1.0302587]]
Q-values after update: [[1.0398906 1.0212766]]
Designated Priority: 1
Q-values before update: [[1.0462525 1.0272288]]
Q-values after update: [[1.0235062 1.0174593]]
Designated Priority: 1
Q-values before update: [[1.0268073 1.0208305]]
Q-values after update: [[1.0057847 1.0109842]]
Designated Priority: 1
Q-values before update: [[1.0062841 1.0119164]]
Q-values after update: [[0.9881382 1.0026846]]
Designated Priority: 1
Q-values before update: [[0.9787502  0.99943143]]
Q-values after update: [[0.95918566 0.9910495 ]]
Designated Priority: 1
Q-values before update: [[0.9618899  0.98811996]]
Q-values after update: [[0.9489134 0.9850856]]
Designated Priority: 1
Q-values before update: [[0.945197   0.98050475]]
Q-values after update: [[0.93534017 0.98041767]]
Designated Priority: 1
Q-values before update: [[0.93317604 0.97819334]]
Q-values after update: [[0.92563426 0.9802679 ]]
Designated Priority: 1
Q-values before update: [[0.92498577 0.9794694 ]]
Q-values after update: [[0.9219799 0.9830234]]
Designated Priority: 1
Q-values before update: [[0.9184059 0.9796728]]
Q-values after update: [[0.91881   0.9839312]]
Designated Priority: 1
Q-values before update: [[0.9091474 0.9786173]]
Q-values after update: [[0.9089121 0.9837402]]
Designated Priority: 1
Q-values before update: [[0.9129065 0.9845344]]
Q-values after update: [[0.9143826  0.99166036]]
Designated Priority: 1
Q-values before update: [[0.91678655 0.99244505]]
Q-values after update: [[0.91865945 0.99997103]]
Designated Priority: 1
Q-values before update: [[0.92225623 1.0031154 ]]
Q-values after update: [[0.9275483 1.0113536]]
Designated Priority: 1
Q-values before update: [[0.9208602 1.0063918]]
Q-values after update: [[0.92550683 1.0142118 ]]
Designated Priority: 1
Q-values before update: [[0.92996013 1.017079  ]]
Q-values after update: [[0.9341753 1.0236832]]
Designated Priority: 1
Q-values before update: [[0.9397706 1.0275376]]
Q-values after update: [[0.9437357 1.033428 ]]
Designated Priority: 1
Q-values before update: [[0.94969803 1.0384691 ]]
Q-values after update: [[0.95321   1.0432465]]
Designated Priority: 1
Q-values before update: [[0.96007085 1.0489984 ]]
Q-values after update: [[0.96292186 1.0521083 ]]
Designated Priority: 1
Q-values before update: [[0.97064996 1.0585468 ]]
Q-values after update: [[0.9726004 1.0594041]]
Designated Priority: 1
Q-values before update: [[0.9811557 1.0664866]]
Q-values after update: [[0.9820976 1.0649273]]
Designated Priority: 1
Q-values before update: [[0.9914373 1.0726023]]
Q-values after update: [[0.99140227 1.0688485 ]]
Designated Priority: 1
Q-values before update: [[0.99889016 1.0732139 ]]
Q-values after update: [[0.9993273 1.0699863]]
Designated Priority: 1
Q-values before update: [[1.0007755 1.0715919]]
Q-values after update: [[1.0002888 1.0664563]]
Designated Priority: 1
Q-values before update: [[1.0065769 1.0689012]]
Q-values after update: [[1.0064741 1.0643501]]
Designated Priority: 1
Q-values before update: [[1.0082228 1.0672066]]
Q-values after update: [[1.0072635 1.060964 ]]
Designated Priority: 1
Q-values before update: [[1.0129291 1.0619266]]
Q-values after update: [[1.0113165 1.0545647]]
Designated Priority: 1
Q-values before update: [[1.0143743 1.0502373]]
Q-values after update: [[1.0133744 1.0437531]]
Designated Priority: 1
Q-values before update: [[1.0200526 1.0526172]]
Q-values after update: [[1.0187894 1.0459718]]
Designated Priority: 1
Q-values before update: [[1.0189444 1.0372027]]
Q-values after update: [[1.0180361 1.0317827]]
Designated Priority: 1
Q-values before update: [[1.0184687 1.0187294]]
Q-values after update: [[1.0191448 1.0170128]]
Designated Priority: 1
Q-values before update: [[1.0205576 1.0038192]]
Q-values after update: [[1.0233796 1.0039304]]
Designated Priority: 1
Q-values before update: [[1.0314832 1.0167407]]
Q-values after update: [[1.0343904 1.0170681]]
Designated Priority: 3
Q-values before update: [[1.0436716 1.0327997]]
Q-values after update: [[1.0322673 1.023637 ]]
Episode 54 out of total 100, Total Reward: 35.0, Epsilon: 0.75, Current State: [ 0.28903022  1.369069   -0.23412466 -1.4393809 ], Steps Taken: 35
Designated Priority: 1
Q-values before update: [[0.98072004 1.0256481 ]]
Q-values after update: [[0.9751363 1.0214498]]
Designated Priority: 1
Q-values before update: [[0.9788631 1.0232831]]
Q-values after update: [[0.9734949 1.018924 ]]
Designated Priority: 1
Q-values before update: [[0.978159  1.0212717]]
Q-values after update: [[0.9730791 1.0170519]]
Designated Priority: 1
Q-values before update: [[0.97868115 1.0198765 ]]
Q-values after update: [[0.9739728 1.0160909]]
Designated Priority: 1
Q-values before update: [[0.98009574 1.0196658 ]]
Q-values after update: [[0.9758332 1.0165813]]
Designated Priority: 1
Q-values before update: [[0.9785155 1.0165248]]
Q-values after update: [[0.9746102 1.0143989]]
Designated Priority: 1
Q-values before update: [[0.97277594 1.002121  ]]
Q-values after update: [[0.9703125 1.0028331]]
Designated Priority: 1
Q-values before update: [[0.9672643 0.9900167]]
Q-values after update: [[0.96757495 0.9956416 ]]
Designated Priority: 3
Q-values before update: [[0.9660686  0.98401874]]
Q-values after update: [[0.97107995 0.99750817]]
Episode 55 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [ 0.12941647  1.7293831  -0.23374748 -2.8206146 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[0.9445859 1.0071193]]
Q-values after update: [[0.94447833 1.0118334 ]]
Designated Priority: 1
Q-values before update: [[0.94754714 1.0133063 ]]
Q-values after update: [[0.9492072 1.0184612]]
Designated Priority: 1
Q-values before update: [[0.9468223 1.017318 ]]
Q-values after update: [[0.94806737 1.0214338 ]]
Designated Priority: 1
Q-values before update: [[0.9514357 1.0234818]]
Q-values after update: [[0.9526439 1.0272437]]
Designated Priority: 1
Q-values before update: [[0.9572629 1.030595 ]]
Q-values after update: [[0.9584018 1.0339596]]
Designated Priority: 1
Q-values before update: [[0.96428275 1.0382614 ]]
Q-values after update: [[0.96530473 1.0411656 ]]
Designated Priority: 1
Q-values before update: [[0.9722612 1.0468284]]
Q-values after update: [[0.97309464 1.0491245 ]]
Designated Priority: 1
Q-values before update: [[0.980403  1.0555472]]
Q-values after update: [[0.98104405 1.0571336 ]]
Designated Priority: 1
Q-values before update: [[0.986164  1.0611739]]
Q-values after update: [[0.98666596 1.0621421 ]]
Designated Priority: 1
Q-values before update: [[0.9888106 1.0601538]]
Q-values after update: [[0.98905545 1.0609639 ]]
Designated Priority: 1
Q-values before update: [[0.99364203 1.0578803 ]]
Q-values after update: [[0.99395686 1.0587682 ]]
Designated Priority: 3
Q-values before update: [[1.0000517 1.0569997]]
Q-values after update: [[0.98610985 1.0284067 ]]
Episode 56 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [ 0.17158036  1.9095722  -0.22638266 -3.0150285 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[0.9556097 1.0271114]]
Q-values after update: [[0.9539964 1.0178086]]
Designated Priority: 1
Q-values before update: [[0.95115614 1.0163114 ]]
Q-values after update: [[0.9500009 1.0081004]]
Designated Priority: 1
Q-values before update: [[0.95105684 1.0076358 ]]
Q-values after update: [[0.9495944 0.9996762]]
Designated Priority: 1
Q-values before update: [[0.9515295  0.99969876]]
Q-values after update: [[0.9499762 0.9924827]]
Designated Priority: 1
Q-values before update: [[0.9525876  0.99277496]]
Q-values after update: [[0.9511423  0.98670673]]
Designated Priority: 1
Q-values before update: [[0.9544437  0.98696184]]
Q-values after update: [[0.9533038 0.9824576]]
Designated Priority: 1
Q-values before update: [[0.95579076 0.98163974]]
Q-values after update: [[0.9549823  0.97892123]]
Designated Priority: 1
Q-values before update: [[0.9528372  0.97218275]]
Q-values after update: [[0.9528343  0.97179884]]
Designated Priority: 1
Q-values before update: [[0.94677186 0.95522964]]
Q-values after update: [[0.9488424 0.9592645]]
Designated Priority: 1
Q-values before update: [[0.9432024 0.9414543]]
Q-values after update: [[0.94990957 0.94802165]]
Designated Priority: 1
Q-values before update: [[0.96225    0.96813893]]
Q-values after update: [[0.9715639 0.976002 ]]
Designated Priority: 3
Q-values before update: [[0.9829478 0.9955205]]
Q-values after update: [[0.99170023 1.0037291 ]]
Episode 57 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [ 0.18488768  1.180316   -0.22540541 -1.9149711 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[0.9608152 0.9985445]]
Q-values after update: [[0.96592575 1.0035793 ]]
Designated Priority: 1
Q-values before update: [[0.967307  1.0023524]]
Q-values after update: [[0.97230625 1.0076475 ]]
Designated Priority: 1
Q-values before update: [[0.9749638 1.007556 ]]
Q-values after update: [[0.97987485 1.0131214 ]]
Designated Priority: 1
Q-values before update: [[0.9837997 1.0136602]]
Q-values after update: [[0.9886484 1.0194969]]
Designated Priority: 1
Q-values before update: [[0.993896  1.0211959]]
Q-values after update: [[0.9986887 1.0272366]]
Designated Priority: 1
Q-values before update: [[1.0044625 1.0295672]]
Q-values after update: [[1.0094367 1.0359498]]
Designated Priority: 1
Q-values before update: [[1.0103178 1.0277681]]
Q-values after update: [[1.0157971 1.035212 ]]
Designated Priority: 1
Q-values before update: [[1.015334  1.0219121]]
Q-values after update: [[1.0218247 1.0297315]]
Designated Priority: 1
Q-values before update: [[1.0314225 1.0471857]]
Q-values after update: [[1.0370145 1.0539151]]
Designated Priority: 1
Q-values before update: [[1.0369593 1.0406377]]
Q-values after update: [[1.0425441 1.0471696]]
Designated Priority: 3
Q-values before update: [[1.0520315 1.0648311]]
Q-values after update: [[1.0461264 1.0477219]]
Episode 58 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.20391831  1.3219022  -0.22408102 -2.133866  ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[0.9951844 1.0368063]]
Q-values after update: [[0.993853  1.0281374]]
Designated Priority: 1
Q-values before update: [[0.9965259 1.02786  ]]
Q-values after update: [[0.9948566 1.0191078]]
Designated Priority: 1
Q-values before update: [[0.9983227 1.0193018]]
Q-values after update: [[0.9965459 1.0110409]]
Designated Priority: 1
Q-values before update: [[1.0016091 1.0128467]]
Q-values after update: [[1.0001714 1.0052854]]
Designated Priority: 1
Q-values before update: [[1.0005765 1.0080831]]
Q-values after update: [[0.9995277 1.0018587]]
Designated Priority: 1
Q-values before update: [[1.0033945 1.0015185]]
Q-values after update: [[1.0025407  0.99579954]]
Designated Priority: 1
Q-values before update: [[1.0040251 1.0005127]]
Q-values after update: [[1.003329  0.9954908]]
Designated Priority: 1
Q-values before update: [[1.0040236 0.9994567]]
Q-values after update: [[1.0034451 0.9951272]]
Designated Priority: 1
Q-values before update: [[1.0032187 0.998379 ]]
Q-values after update: [[1.0030957 0.9947663]]
Designated Priority: 1
Q-values before update: [[1.0019585  0.99738973]]
Q-values after update: [[1.0020059 0.9944521]]
Designated Priority: 1
Q-values before update: [[1.0019794  0.99091077]]
Q-values after update: [[1.0022748 0.9882517]]
Designated Priority: 1
Q-values before update: [[1.0014105 0.9912367]]
Q-values after update: [[1.0024912 0.9892391]]
Designated Priority: 1
Q-values before update: [[1.0007001  0.99157643]]
Q-values after update: [[1.0028936 0.9903265]]
Designated Priority: 1
Q-values before update: [[0.99948335 0.9925859 ]]
Q-values after update: [[1.0031613  0.99220043]]
Designated Priority: 1
Q-values before update: [[0.98833925 0.9901135 ]]
Q-values after update: [[0.9925688 0.9918599]]
Designated Priority: 1
Q-values before update: [[0.9996173 0.9885262]]
Q-values after update: [[1.0036945 0.9913075]]
Designated Priority: 1
Q-values before update: [[1.0018557  0.98441315]]
Q-values after update: [[1.0065496 0.987155 ]]
Designated Priority: 1
Q-values before update: [[1.0031061  0.99085087]]
Q-values after update: [[1.0080346  0.99501085]]
Designated Priority: 1
Q-values before update: [[1.0060266 0.987234 ]]
Q-values after update: [[1.0114411  0.99119794]]
Designated Priority: 1
Q-values before update: [[1.0041752 0.9934219]]
Q-values after update: [[1.0111029  0.99801236]]
Designated Priority: 1
Q-values before update: [[0.97842145 0.9868767 ]]
Q-values after update: [[0.9859518 0.9936943]]
Designated Priority: 1
Q-values before update: [[0.9997002  0.99295366]]
Q-values after update: [[1.0070679 1.0006803]]
Designated Priority: 1
Q-values before update: [[1.0168498 1.0002793]]
Q-values after update: [[1.0239248 1.0071486]]
Designated Priority: 1
Q-values before update: [[0.99814403 0.9982846 ]]
Q-values after update: [[1.006013  1.0069373]]
Designated Priority: 1
Q-values before update: [[1.0154788 1.0061669]]
Q-values after update: [[1.0228152 1.0148324]]
Designated Priority: 1
Q-values before update: [[1.0282729 1.0118312]]
Q-values after update: [[1.0347731 1.0192611]]
Designated Priority: 3
Q-values before update: [[1.0142502 1.0141664]]
Q-values after update: [[1.017918  1.0202718]]
Episode 59 out of total 100, Total Reward: 27.0, Epsilon: 0.75, Current State: [-0.15408024 -0.60952055  0.22128609  1.2541189 ], Steps Taken: 27
Designated Priority: 1
Q-values before update: [[1.0648226 1.0321859]]
Q-values after update: [[1.0654331 1.0361638]]
Designated Priority: 1
Q-values before update: [[1.0688511 1.043767 ]]
Q-values after update: [[1.0689933 1.0459557]]
Designated Priority: 1
Q-values before update: [[1.0648268 1.0376239]]
Q-values after update: [[1.0626866 1.0386335]]
Designated Priority: 1
Q-values before update: [[1.0663027 1.046532 ]]
Q-values after update: [[1.0624884 1.0468357]]
Designated Priority: 1
Q-values before update: [[1.0640411 1.05482  ]]
Q-values after update: [[1.0590076 1.0545805]]
Designated Priority: 1
Q-values before update: [[1.0554941 1.0609149]]
Q-values after update: [[1.0501666 1.0586115]]
Designated Priority: 1
Q-values before update: [[1.0479995 1.0490289]]
Q-values after update: [[1.0426934 1.0452347]]
Designated Priority: 1
Q-values before update: [[1.0387714 1.0346435]]
Q-values after update: [[1.0331569 1.0309442]]
Designated Priority: 1
Q-values before update: [[1.0331893 1.0397931]]
Q-values after update: [[1.0276091 1.0350642]]
Designated Priority: 1
Q-values before update: [[1.0236797 1.0246074]]
Q-values after update: [[1.0184095 1.0203159]]
Designated Priority: 1
Q-values before update: [[1.0140066 1.0262691]]
Q-values after update: [[1.0088612 1.0215325]]
Designated Priority: 1
Q-values before update: [[1.0089679 1.0138756]]
Q-values after update: [[1.0042514 1.0090553]]
Designated Priority: 1
Q-values before update: [[1.0016625 1.0001353]]
Q-values after update: [[0.99771106 0.9960119 ]]
Designated Priority: 1
Q-values before update: [[0.99728703 1.0041108 ]]
Q-values after update: [[0.993523   0.99996555]]
Designated Priority: 1
Q-values before update: [[0.99129856 0.9919368 ]]
Q-values after update: [[0.9880924  0.98859274]]
Designated Priority: 1
Q-values before update: [[0.98832965 0.98267925]]
Q-values after update: [[0.98574674 0.9798168 ]]
Designated Priority: 3
Q-values before update: [[0.9843017 0.9867333]]
Q-values after update: [[0.98277736 0.98654187]]
Episode 60 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [-0.02728765  0.21510765  0.22061053  0.37506774], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[1.0081694 1.002796 ]]
Q-values after update: [[1.0067866 1.0026982]]
Designated Priority: 1
Q-values before update: [[1.0046846 0.9957887]]
Q-values after update: [[1.0032995 0.9956552]]
Designated Priority: 1
Q-values before update: [[1.0064535 1.0033568]]
Q-values after update: [[1.0051976 1.0032276]]
Designated Priority: 1
Q-values before update: [[1.0072986 1.0101469]]
Q-values after update: [[1.0060277 1.0096388]]
Designated Priority: 1
Q-values before update: [[1.0029334 1.0019834]]
Q-values after update: [[1.0019302 1.0015863]]
Designated Priority: 1
Q-values before update: [[1.0039824 1.0084662]]
Q-values after update: [[1.0029573 1.007767 ]]
Designated Priority: 1
Q-values before update: [[0.9998863 1.0001372]]
Q-values after update: [[0.99919367 0.9996027 ]]
Designated Priority: 1
Q-values before update: [[1.0011904 1.0064303]]
Q-values after update: [[1.0004649 1.0056626]]
Designated Priority: 1
Q-values before update: [[0.9974016 0.9980514]]
Q-values after update: [[0.99687696 0.99772894]]
Designated Priority: 1
Q-values before update: [[0.9948189  0.99086547]]
Q-values after update: [[0.99445546 0.99062395]]
Designated Priority: 1
Q-values before update: [[0.99735546 0.9980943 ]]
Q-values after update: [[0.99711776 0.99817973]]
Designated Priority: 1
Q-values before update: [[0.99503    0.99129117]]
Q-values after update: [[0.9949162 0.9914103]]
Designated Priority: 1
Q-values before update: [[0.9977453  0.99881387]]
Q-values after update: [[0.9977211 0.999185 ]]
Designated Priority: 1
Q-values before update: [[0.9956062  0.99227065]]
Q-values after update: [[0.9956646  0.99263746]]
Designated Priority: 1
Q-values before update: [[0.9984355 0.9999887]]
Q-values after update: [[0.99869287 1.0003895 ]]
Designated Priority: 1
Q-values before update: [[1.0007724 1.0071086]]
Q-values after update: [[1.0008914 1.0071349]]
Designated Priority: 1
Q-values before update: [[0.99740785 0.99932504]]
Q-values after update: [[0.99758214 0.99954236]]
Designated Priority: 1
Q-values before update: [[0.9954317  0.99260455]]
Q-values after update: [[0.99566835 0.9928342 ]]
Designated Priority: 1
Q-values before update: [[0.9984095 1.0001204]]
Q-values after update: [[0.9986622 1.0004638]]
Designated Priority: 1
Q-values before update: [[0.99641013 0.9934689 ]]
Q-values after update: [[0.99668324 0.99379814]]
Designated Priority: 1
Q-values before update: [[0.9994849 1.0010769]]
Q-values after update: [[0.9997783 1.0015315]]
Designated Priority: 1
Q-values before update: [[0.9973719 0.9944572]]
Q-values after update: [[0.99764305 0.9948708 ]]
Designated Priority: 1
Q-values before update: [[1.0005114 1.0021507]]
Q-values after update: [[1.0008132 1.0027102]]
Designated Priority: 1
Q-values before update: [[0.9982519 0.9955539]]
Q-values after update: [[0.9984958 0.9960475]]
Designated Priority: 1
Q-values before update: [[1.001438  1.0033367]]
Q-values after update: [[1.0017271 1.0040035]]
Designated Priority: 1
Q-values before update: [[0.9990407 0.9967736]]
Q-values after update: [[0.99924135 0.9973503 ]]
Designated Priority: 1
Q-values before update: [[1.0022326 1.0046439]]
Q-values after update: [[1.0024908 1.0054076]]
Designated Priority: 1
Q-values before update: [[0.9997663 0.9981351]]
Q-values after update: [[0.99990827 0.9987859 ]]
Designated Priority: 1
Q-values before update: [[1.0028628 1.0060544]]
Q-values after update: [[1.0030638 1.006871 ]]
Designated Priority: 1
Q-values before update: [[1.0003003 0.999552 ]]
Q-values after update: [[1.0003643 1.0002394]]
Designated Priority: 1
Q-values before update: [[1.0032839 1.0074863]]
Q-values after update: [[1.0032829 1.0080901]]
Designated Priority: 1
Q-values before update: [[1.0050588 1.0146761]]
Q-values after update: [[1.0048321 1.014528 ]]
Designated Priority: 1
Q-values before update: [[1.001154  1.0063263]]
Q-values after update: [[1.0010517 1.0065033]]
Designated Priority: 1
Q-values before update: [[0.9982557 0.9991386]]
Q-values after update: [[0.99829495 0.9996933 ]]
Designated Priority: 1
Q-values before update: [[0.99647665 0.9930493 ]]
Q-values after update: [[0.9970169 0.9937404]]
Designated Priority: 1
Q-values before update: [[1.0008024 1.0016031]]
Q-values after update: [[1.0014205 1.0026453]]
Designated Priority: 1
Q-values before update: [[0.9995245 0.9959333]]
Q-values after update: [[1.0004531  0.99701536]]
Designated Priority: 1
Q-values before update: [[1.0041392 1.0047911]]
Q-values after update: [[1.0051101 1.0061939]]
Designated Priority: 1
Q-values before update: [[1.0031538 0.9994284]]
Q-values after update: [[1.0042695 1.0007868]]
Designated Priority: 1
Q-values before update: [[1.0078707 1.0084901]]
Q-values after update: [[1.0084878 1.0095687]]
Designated Priority: 1
Q-values before update: [[1.0110427 1.0164877]]
Q-values after update: [[1.0115154 1.0172255]]
Designated Priority: 1
Q-values before update: [[1.0085062 1.009664 ]]
Q-values after update: [[1.0090821 1.0107687]]
Designated Priority: 1
Q-values before update: [[1.0070777 1.0039543]]
Q-values after update: [[1.0076941 1.0049897]]
Designated Priority: 1
Q-values before update: [[1.0111735 1.0125879]]
Q-values after update: [[1.0118651 1.0139543]]
Designated Priority: 1
Q-values before update: [[1.0098144 1.0070944]]
Q-values after update: [[1.0106032 1.0088041]]
Designated Priority: 1
Q-values before update: [[1.0095209 1.0024718]]
Q-values after update: [[1.0107555 1.0042167]]
Designated Priority: 1
Q-values before update: [[1.0151894 1.0128323]]
Q-values after update: [[1.0160155 1.014291 ]]
Designated Priority: 1
Q-values before update: [[1.0192935 1.0216801]]
Q-values after update: [[1.0200781 1.0231411]]
Designated Priority: 1
Q-values before update: [[1.018062  1.0165349]]
Q-values after update: [[1.0183972 1.017709 ]]
Designated Priority: 1
Q-values before update: [[1.0216336 1.0250726]]
Q-values after update: [[1.021943 1.026175]]
Designated Priority: 1
Q-values before update: [[1.0199248 1.01956  ]]
Q-values after update: [[1.0197654 1.0203817]]
Designated Priority: 1
Q-values before update: [[1.0229962 1.0277858]]
Q-values after update: [[1.0228322 1.0284851]]
Designated Priority: 1
Q-values before update: [[1.0207858 1.0218053]]
Q-values after update: [[1.0207409 1.0227226]]
Designated Priority: 1
Q-values before update: [[1.0195583 1.0159646]]
Q-values after update: [[1.0197991 1.0169063]]
Designated Priority: 1
Q-values before update: [[1.024166  1.0259626]]
Q-values after update: [[1.0244343 1.0269835]]
Designated Priority: 1
Q-values before update: [[1.0231805 1.0199525]]
Q-values after update: [[1.0236087 1.020951 ]]
Designated Priority: 1
Q-values before update: [[1.0279483 1.0300037]]
Q-values after update: [[1.0283287 1.0309076]]
Designated Priority: 1
Q-values before update: [[1.0270543 1.0238128]]
Q-values after update: [[1.0274606 1.0246575]]
Designated Priority: 1
Q-values before update: [[1.0316095 1.0335126]]
Q-values after update: [[1.0318944 1.0340602]]
Designated Priority: 1
Q-values before update: [[1.0306925 1.0269954]]
Q-values after update: [[1.0308764 1.02746  ]]
Designated Priority: 1
Q-values before update: [[1.034748  1.0365114]]
Q-values after update: [[1.0347508 1.0364765]]
Designated Priority: 1
Q-values before update: [[1.0336506 1.028972 ]]
Q-values after update: [[1.0333493 1.0288051]]
Designated Priority: 1
Q-values before update: [[1.0371763 1.0383825]]
Q-values after update: [[1.0366728 1.0375556]]
Designated Priority: 1
Q-values before update: [[1.034904  1.0291071]]
Q-values after update: [[1.0339367 1.0281076]]
Designated Priority: 1
Q-values before update: [[1.0386436 1.0388093]]
Q-values after update: [[1.0374626 1.0369998]]
Designated Priority: 1
Q-values before update: [[1.034748  1.0273296]]
Q-values after update: [[1.0329316 1.0253   ]]
Designated Priority: 1
Q-values before update: [[1.0388591 1.0375057]]
Q-values after update: [[1.0365624 1.0354332]]
Designated Priority: 1
Q-values before update: [[1.0398962 1.0447414]]
Q-values after update: [[1.0372736 1.0413439]]
Designated Priority: 1
Q-values before update: [[1.0351992 1.0329844]]
Q-values after update: [[1.0319927 1.029547 ]]
Designated Priority: 1
Q-values before update: [[1.0353475 1.0389478]]
Q-values after update: [[1.0318996 1.0343374]]
Designated Priority: 1
Q-values before update: [[1.0298887 1.0262003]]
Q-values after update: [[1.0266094 1.0216222]]
Designated Priority: 1
Q-values before update: [[1.017419  1.0025736]]
Q-values after update: [[1.0139036 0.9981203]]
Designated Priority: 1
Q-values before update: [[1.0253801 1.0193312]]
Q-values after update: [[1.0215514 1.01499  ]]
Designated Priority: 1
Q-values before update: [[1.026329  1.0279603]]
Q-values after update: [[1.022613  1.0232341]]
Designated Priority: 1
Q-values before update: [[1.0174125 1.0103357]]
Q-values after update: [[1.0138137 1.0058949]]
Designated Priority: 3
Q-values before update: [[1.0212038 1.0222677]]
Q-values after update: [[1.015735  1.0124191]]
Episode 61 out of total 100, Total Reward: 76.0, Epsilon: 0.75, Current State: [ 0.34080893  0.4090383  -0.21798874 -0.89769745], Steps Taken: 76
Designated Priority: 1
Q-values before update: [[0.9826014 0.9977342]]
Q-values after update: [[0.97953224 0.9920243 ]]
Designated Priority: 1
Q-values before update: [[0.97752726 0.98519063]]
Q-values after update: [[0.975518  0.9803326]]
Designated Priority: 1
Q-values before update: [[0.978351  0.9877341]]
Q-values after update: [[0.9767707 0.9840194]]
Designated Priority: 1
Q-values before update: [[0.9746628  0.97711337]]
Q-values after update: [[0.9736099 0.9749898]]
Designated Priority: 1
Q-values before update: [[0.97217596 0.96803737]]
Q-values after update: [[0.97222906 0.9664558 ]]
Designated Priority: 1
Q-values before update: [[0.9760208  0.97494936]]
Q-values after update: [[0.97683656 0.9738096 ]]
Designated Priority: 1
Q-values before update: [[0.97963613 0.9811182 ]]
Q-values after update: [[0.9806373 0.9809199]]
Designated Priority: 1
Q-values before update: [[0.97843784 0.9739517 ]]
Q-values after update: [[0.9800272  0.97402066]]
Designated Priority: 1
Q-values before update: [[0.9828274 0.9813108]]
Q-values after update: [[0.9851035 0.981664 ]]
Designated Priority: 1
Q-values before update: [[0.98710346 0.98844326]]
Q-values after update: [[0.98930484 0.98919296]]
Designated Priority: 1
Q-values before update: [[0.9862834 0.9817294]]
Q-values after update: [[0.98900247 0.9826672 ]]
Designated Priority: 1
Q-values before update: [[0.99105155 0.9894848 ]]
Q-values after update: [[0.9944768 0.9906839]]
Designated Priority: 1
Q-values before update: [[0.9958565 0.997169 ]]
Q-values after update: [[1.000181   0.99871206]]
Designated Priority: 1
Q-values before update: [[0.9992044 1.00636  ]]
Q-values after update: [[1.003375  1.0083959]]
Designated Priority: 1
Q-values before update: [[0.9998521  0.99850786]]
Q-values after update: [[1.0046582 1.0007087]]
Designated Priority: 1
Q-values before update: [[1.0038056 1.0086163]]
Q-values after update: [[1.0084447 1.0112785]]
Designated Priority: 1
Q-values before update: [[1.0046829 1.0013728]]
Q-values after update: [[1.009786  1.0040797]]
Designated Priority: 1
Q-values before update: [[1.0033382 1.0086048]]
Q-values after update: [[1.0083433 1.0118756]]
Designated Priority: 1
Q-values before update: [[1.009963  1.0055243]]
Q-values after update: [[1.0152494 1.0087073]]
Designated Priority: 1
Q-values before update: [[1.0001669 1.0079445]]
Q-values after update: [[1.0069746 1.0117644]]
Designated Priority: 1
Q-values before update: [[0.97449327 1.0050255 ]]
Q-values after update: [[0.9815537 1.0102909]]
Designated Priority: 1
Q-values before update: [[0.9946338 1.006612 ]]
Q-values after update: [[1.0014497 1.0125484]]
Designated Priority: 1
Q-values before update: [[1.0093564 1.0104177]]
Q-values after update: [[1.0167527 1.0162069]]
Designated Priority: 3
Q-values before update: [[0.9909493 1.0094968]]
Q-values after update: [[0.9968964 1.0127313]]
Episode 62 out of total 100, Total Reward: 24.0, Epsilon: 0.75, Current State: [-0.13079016 -0.4089581   0.22636287  0.990114  ], Steps Taken: 24
Designated Priority: 1
Q-values before update: [[1.0566843 1.023704 ]]
Q-values after update: [[1.0598844 1.0254822]]
Designated Priority: 1
Q-values before update: [[1.0636125 1.0338573]]
Q-values after update: [[1.06531   1.0350684]]
Designated Priority: 1
Q-values before update: [[1.0683594 1.0430933]]
Q-values after update: [[1.0688659 1.0438303]]
Designated Priority: 1
Q-values before update: [[1.0700245 1.0525255]]
Q-values after update: [[1.0697706 1.0529199]]
Designated Priority: 1
Q-values before update: [[1.06099   1.0588553]]
Q-values after update: [[1.0610299 1.0593756]]
Designated Priority: 1
Q-values before update: [[1.0283065 1.0547175]]
Q-values after update: [[1.0309256 1.0563703]]
Designated Priority: 1
Q-values before update: [[0.99893904 1.0521841 ]]
Q-values after update: [[1.0018091 1.0545759]]
Designated Priority: 1
Q-values before update: [[1.0115246 1.0470736]]
Q-values after update: [[1.014301  1.0497618]]
Designated Priority: 1
Q-values before update: [[1.0275159 1.0442834]]
Q-values after update: [[1.0300264 1.046966 ]]
Designated Priority: 1
Q-values before update: [[1.0406138 1.0427302]]
Q-values after update: [[1.0427336 1.0451646]]
Designated Priority: 1
Q-values before update: [[1.0501324 1.0422932]]
Q-values after update: [[1.0517838 1.0440571]]
Designated Priority: 1
Q-values before update: [[1.0468816 1.0333426]]
Q-values after update: [[1.0481324 1.034716 ]]
Designated Priority: 3
Q-values before update: [[1.0405378 1.0398647]]
Q-values after update: [[1.0329463 1.037344 ]]
Episode 63 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.16904542 -0.62224656  0.20993048  1.1944838 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.061309  1.0345659]]
Q-values after update: [[1.0543201 1.032578 ]]
Designated Priority: 1
Q-values before update: [[1.0589588 1.0420392]]
Q-values after update: [[1.0516424 1.0398338]]
Designated Priority: 1
Q-values before update: [[1.0553569 1.0487629]]
Q-values after update: [[1.0482409 1.0465392]]
Designated Priority: 1
Q-values before update: [[1.050137  1.0557698]]
Q-values after update: [[1.0432796 1.0528008]]
Designated Priority: 1
Q-values before update: [[1.0376651 1.0414765]]
Q-values after update: [[1.0319345 1.0389843]]
Designated Priority: 1
Q-values before update: [[1.0332417 1.0484376]]
Q-values after update: [[1.0278019 1.0456525]]
Designated Priority: 1
Q-values before update: [[1.0228393 1.0342208]]
Q-values after update: [[1.0189428 1.0321226]]
Designated Priority: 1
Q-values before update: [[1.0194949 1.041928 ]]
Q-values after update: [[1.0158443 1.0398273]]
Designated Priority: 1
Q-values before update: [[1.0110966 1.0284932]]
Q-values after update: [[1.0078926 1.0266886]]
Designated Priority: 1
Q-values before update: [[1.0031195 1.0166798]]
Q-values after update: [[1.0003854 1.0153365]]
Designated Priority: 1
Q-values before update: [[0.9959347 1.0062789]]
Q-values after update: [[0.9936533 1.0054998]]
Designated Priority: 1
Q-values before update: [[0.9910387  0.99861866]]
Q-values after update: [[0.98930407 0.9987788 ]]
Designated Priority: 1
Q-values before update: [[0.9878168  0.99292606]]
Q-values after update: [[0.98661053 0.9940372 ]]
Designated Priority: 1
Q-values before update: [[0.98574626 0.98838955]]
Q-values after update: [[0.98513156 0.99065316]]
Designated Priority: 1
Q-values before update: [[0.984599   0.98416233]]
Q-values after update: [[0.98506796 0.98666084]]
Designated Priority: 1
Q-values before update: [[0.9895438  0.99442554]]
Q-values after update: [[0.990237   0.99762017]]
Designated Priority: 1
Q-values before update: [[0.98967296 0.9910378 ]]
Q-values after update: [[0.990888  0.9954139]]
Designated Priority: 1
Q-values before update: [[0.9874668  0.98292863]]
Q-values after update: [[0.9898756  0.98757154]]
Designated Priority: 1
Q-values before update: [[0.99787873 1.0008631 ]]
Q-values after update: [[1.0002177 1.0058339]]
Designated Priority: 1
Q-values before update: [[0.9956178  0.99110866]]
Q-values after update: [[0.99867463 0.99773514]]
Designated Priority: 1
Q-values before update: [[0.98803383 0.9688828 ]]
Q-values after update: [[0.9927653 0.9790546]]
Designated Priority: 1
Q-values before update: [[0.97939   0.9508256]]
Q-values after update: [[0.9879805  0.96543586]]
Designated Priority: 1
Q-values before update: [[0.9699298 0.9401628]]
Q-values after update: [[0.98422146 0.96304667]]
Designated Priority: 1
Q-values before update: [[0.9645169 0.9350221]]
Q-values after update: [[0.9858159 0.9631903]]
Designated Priority: 3
Q-values before update: [[0.997403   0.97360396]]
Q-values after update: [[1.016732  0.9989834]]
Episode 64 out of total 100, Total Reward: 25.0, Epsilon: 0.75, Current State: [ 0.14553212  1.323964   -0.24850139 -1.9893627 ], Steps Taken: 25
Designated Priority: 1
Q-values before update: [[1.039071  1.0938754]]
Q-values after update: [[1.0438104 1.1009216]]
Designated Priority: 1
Q-values before update: [[1.0442904 1.0969343]]
Q-values after update: [[1.0479404 1.1004395]]
Designated Priority: 1
Q-values before update: [[1.0496984 1.0968908]]
Q-values after update: [[1.0522652 1.0971607]]
Designated Priority: 1
Q-values before update: [[1.0554621 1.0948663]]
Q-values after update: [[1.0570035 1.0923804]]
Designated Priority: 1
Q-values before update: [[1.0622776 1.0923796]]
Q-values after update: [[1.062732  1.0874261]]
Designated Priority: 1
Q-values before update: [[1.0664575 1.0786388]]
Q-values after update: [[1.066874  1.0734725]]
Designated Priority: 1
Q-values before update: [[1.065322  1.0558813]]
Q-values after update: [[1.0642192 1.0506097]]
Designated Priority: 1
Q-values before update: [[1.0688945 1.0617502]]
Q-values after update: [[1.0670905 1.0553871]]
Designated Priority: 3
Q-values before update: [[1.0652918 1.0375313]]
Q-values after update: [[1.0437356 1.019839 ]]
Episode 65 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [ 0.12719719  0.9937748  -0.2392678  -1.7677357 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0198109 1.0532101]]
Q-values after update: [[1.0076253 1.0422566]]
Designated Priority: 1
Q-values before update: [[1.008114  1.0386771]]
Q-values after update: [[0.99647474 1.0275708 ]]
Designated Priority: 1
Q-values before update: [[0.99793196 1.0251707 ]]
Q-values after update: [[0.98709005 1.0147562 ]]
Designated Priority: 1
Q-values before update: [[0.98904485 1.0122428 ]]
Q-values after update: [[0.97915685 1.0031333 ]]
Designated Priority: 1
Q-values before update: [[0.9812131 1.0002704]]
Q-values after update: [[0.9724918  0.99311346]]
Designated Priority: 1
Q-values before update: [[0.9731288  0.98848146]]
Q-values after update: [[0.96650594 0.98235875]]
Designated Priority: 1
Q-values before update: [[0.9712545 0.9881243]]
Q-values after update: [[0.9672897 0.9836538]]
Designated Priority: 1
Q-values before update: [[0.97018313 0.9882884 ]]
Q-values after update: [[0.9672997  0.98576385]]
Designated Priority: 1
Q-values before update: [[0.9662131 0.9800172]]
Q-values after update: [[0.9640986  0.97957796]]
Designated Priority: 1
Q-values before update: [[0.95669645 0.9644425 ]]
Q-values after update: [[0.9560598 0.9675863]]
Designated Priority: 1
Q-values before update: [[0.9469255  0.94441026]]
Q-values after update: [[0.9490112 0.9531338]]
Designated Priority: 1
Q-values before update: [[0.9397565  0.92943525]]
Q-values after update: [[0.94714534 0.9411763 ]]
Designated Priority: 3
Q-values before update: [[0.95459616 0.95313644]]
Q-values after update: [[0.97229564 0.9702538 ]]
Episode 66 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.1896522   0.9873133  -0.23953253 -1.6374933 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[0.97424185 1.0202084 ]]
Q-values after update: [[0.98298866 1.0271027 ]]
Designated Priority: 1
Q-values before update: [[0.9828843 1.0234947]]
Q-values after update: [[0.99123526 1.0299981 ]]
Designated Priority: 1
Q-values before update: [[0.9928763 1.0281985]]
Q-values after update: [[1.0014687 1.0348363]]
Designated Priority: 1
Q-values before update: [[1.0017881 1.0374911]]
Q-values after update: [[1.008861  1.0421324]]
Designated Priority: 1
Q-values before update: [[1.0109591 1.0405672]]
Q-values after update: [[1.0175151 1.0444038]]
Designated Priority: 1
Q-values before update: [[1.021873  1.0451998]]
Q-values after update: [[1.0279099 1.0483032]]
Designated Priority: 1
Q-values before update: [[1.0332812 1.0494993]]
Q-values after update: [[1.038779  1.0518308]]
Designated Priority: 1
Q-values before update: [[1.0451698 1.0535808]]
Q-values after update: [[1.0501243 1.055186 ]]
Designated Priority: 1
Q-values before update: [[1.0544808 1.0506234]]
Q-values after update: [[1.058643  1.0526619]]
Designated Priority: 1
Q-values before update: [[1.0608351 1.0578855]]
Q-values after update: [[1.0624973 1.0581895]]
Designated Priority: 1
Q-values before update: [[1.0633377 1.0600468]]
Q-values after update: [[1.0627575 1.0591596]]
Designated Priority: 1
Q-values before update: [[1.0638239 1.0622251]]
Q-values after update: [[1.0611619 1.0604374]]
Designated Priority: 3
Q-values before update: [[1.0615755 1.0631766]]
Q-values after update: [[1.0536923 1.0470437]]
Episode 67 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.16545542  0.64085805 -0.21936421 -1.1680713 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0211489 1.0398278]]
Q-values after update: [[1.0155289 1.0273491]]
Designated Priority: 1
Q-values before update: [[1.0134039 1.0286703]]
Q-values after update: [[1.0081959 1.0166283]]
Designated Priority: 1
Q-values before update: [[1.0095755 1.0149486]]
Q-values after update: [[1.0047002 1.0038745]]
Designated Priority: 1
Q-values before update: [[1.0066817 1.002401 ]]
Q-values after update: [[1.0018718 0.9922136]]
Designated Priority: 1
Q-values before update: [[1.0010822 0.9945977]]
Q-values after update: [[0.9976069  0.98590064]]
Designated Priority: 1
Q-values before update: [[0.9962344  0.98808753]]
Q-values after update: [[0.9947553  0.98099864]]
Designated Priority: 1
Q-values before update: [[0.9928214 0.9830108]]
Q-values after update: [[0.99368995 0.9775688 ]]
Designated Priority: 1
Q-values before update: [[0.9911171 0.9795306]]
Q-values after update: [[0.99464333 0.9757823 ]]
Designated Priority: 1
Q-values before update: [[0.9894481 0.9791144]]
Q-values after update: [[0.9961792  0.97717565]]
Designated Priority: 1
Q-values before update: [[0.9616966  0.96865165]]
Q-values after update: [[0.9736916 0.9696166]]
Designated Priority: 1
Q-values before update: [[0.9390811 0.9616395]]
Q-values after update: [[0.9534077  0.96932507]]
Designated Priority: 1
Q-values before update: [[0.9683105  0.96741384]]
Q-values after update: [[0.98286086 0.9783567 ]]
Designated Priority: 1
Q-values before update: [[1.0001236  0.97820747]]
Q-values after update: [[1.0163776 0.98892  ]]
Designated Priority: 1
Q-values before update: [[0.9823784 0.9827159]]
Q-values after update: [[1.0039619 0.9960666]]
Designated Priority: 1
Q-values before update: [[0.97169304 0.9913713 ]]
Q-values after update: [[0.9957236 1.010432 ]]
Designated Priority: 3
Q-values before update: [[1.003737 1.004855]]
Q-values after update: [[1.0239587 1.0199116]]
Episode 68 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [-0.23841463 -0.8188601   0.21022333  1.2487656 ], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[1.0762525 0.9951091]]
Q-values after update: [[1.0847229 1.0015805]]
Designated Priority: 1
Q-values before update: [[1.0904355 1.0104138]]
Q-values after update: [[1.0960305 1.0159582]]
Designated Priority: 1
Q-values before update: [[1.1015956 1.025582 ]]
Q-values after update: [[1.1042484 1.0300705]]
Designated Priority: 1
Q-values before update: [[1.1084565 1.0419391]]
Q-values after update: [[1.1082404 1.0452904]]
Designated Priority: 1
Q-values before update: [[1.1012597 1.0511371]]
Q-values after update: [[1.0998319 1.0539925]]
Designated Priority: 1
Q-values before update: [[1.0769463 1.0570968]]
Q-values after update: [[1.0748765 1.0595746]]
Designated Priority: 1
Q-values before update: [[1.0503867 1.0623987]]
Q-values after update: [[1.0483043 1.063901 ]]
Designated Priority: 3
Q-values before update: [[1.050761  1.0532618]]
Q-values after update: [[1.0412031 1.0387659]]
Episode 69 out of total 100, Total Reward: 8.0, Epsilon: 0.75, Current State: [-0.07366998 -0.7806259   0.21512209  1.4258373 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[1.0827838 1.0131669]]
Q-values after update: [[1.0743682 1.0029862]]
Designated Priority: 1
Q-values before update: [[1.080394  1.0126257]]
Q-values after update: [[1.0706457 1.0023859]]
Designated Priority: 1
Q-values before update: [[1.0757307 1.0114061]]
Q-values after update: [[1.0653377 1.001334 ]]
Designated Priority: 1
Q-values before update: [[1.0687418 1.0108926]]
Q-values after update: [[1.0584912 1.0011808]]
Designated Priority: 1
Q-values before update: [[1.0617158 1.0123466]]
Q-values after update: [[1.0523196 1.0033562]]
Designated Priority: 1
Q-values before update: [[1.0374435 1.0077089]]
Q-values after update: [[1.0304103  0.99990386]]
Designated Priority: 1
Q-values before update: [[1.0050768  0.99980813]]
Q-values after update: [[1.00303    0.99459195]]
Designated Priority: 1
Q-values before update: [[0.9758134 0.9934399]]
Q-values after update: [[0.9818013 0.992471 ]]
Designated Priority: 1
Q-values before update: [[0.95320034 0.99062055]]
Q-values after update: [[0.96313643 0.99751174]]
Designated Priority: 3
Q-values before update: [[0.9641074 0.9853567]]
Q-values after update: [[0.9844668  0.99715227]]
Episode 70 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.18131341 -1.5802783   0.21946958  2.48838   ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0350168 0.9536808]]
Q-values after update: [[1.0425593 0.9581637]]
Designated Priority: 1
Q-values before update: [[1.0354128 0.9484461]]
Q-values after update: [[1.0404749  0.95149434]]
Designated Priority: 1
Q-values before update: [[1.0488392  0.96205854]]
Q-values after update: [[1.0528902 0.964955 ]]
Designated Priority: 1
Q-values before update: [[1.0615255 0.9760337]]
Q-values after update: [[1.064702   0.97880274]]
Designated Priority: 1
Q-values before update: [[1.0743685 0.9907553]]
Q-values after update: [[1.0780988 0.9945438]]
Designated Priority: 1
Q-values before update: [[1.0660889 0.9817422]]
Q-values after update: [[1.0674894 0.9841671]]
Designated Priority: 1
Q-values before update: [[1.0783917  0.99717283]]
Q-values after update: [[1.0784808 0.9991201]]
Designated Priority: 1
Q-values before update: [[1.0891986 1.0140941]]
Q-values after update: [[1.0879085 1.0155282]]
Designated Priority: 1
Q-values before update: [[1.0984124 1.03288  ]]
Q-values after update: [[1.0956645 1.0336194]]
Designated Priority: 1
Q-values before update: [[1.0974972 1.0465248]]
Q-values after update: [[1.0944955 1.0469667]]
Designated Priority: 1
Q-values before update: [[1.082386 1.056572]]
Q-values after update: [[1.0796552 1.0570234]]
Designated Priority: 1
Q-values before update: [[1.0662148 1.066149 ]]
Q-values after update: [[1.065633  1.0676082]]
Designated Priority: 3
Q-values before update: [[1.0509253 1.0763153]]
Q-values after update: [[1.0336318 1.0451105]]
Episode 71 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.1404348  -1.4227742   0.24639304  2.3056204 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0330783  0.95594984]]
Q-values after update: [[1.0260097 0.9430287]]
Designated Priority: 1
Q-values before update: [[1.0358497 0.9543403]]
Q-values after update: [[1.0283766 0.9416934]]
Designated Priority: 1
Q-values before update: [[1.0374732 0.9521774]]
Q-values after update: [[1.0300418  0.94002575]]
Designated Priority: 1
Q-values before update: [[1.0379908 0.949517 ]]
Q-values after update: [[1.0310369 0.9380528]]
Designated Priority: 1
Q-values before update: [[1.037993   0.94686794]]
Q-values after update: [[1.0320312 0.936188 ]]
Designated Priority: 1
Q-values before update: [[1.0376441 0.945763 ]]
Q-values after update: [[1.0330775  0.93614316]]
Designated Priority: 1
Q-values before update: [[1.0227891 0.9360442]]
Q-values after update: [[1.0208716  0.92777485]]
Designated Priority: 1
Q-values before update: [[1.0024126 0.9264662]]
Q-values after update: [[1.0052205 0.9208845]]
Designated Priority: 1
Q-values before update: [[0.9850215  0.91844153]]
Q-values after update: [[0.99490356 0.9168941 ]]
Designated Priority: 3
Q-values before update: [[0.97342277 0.9136598 ]]
Q-values after update: [[0.9925837 0.9175111]]
Episode 72 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.15126589 -1.9763435   0.23615547  3.0130126 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.017775  0.8850461]]
Q-values after update: [[1.0266603 0.8878491]]
Designated Priority: 1
Q-values before update: [[1.0184495 0.8802994]]
Q-values after update: [[1.0272942  0.88631743]]
Designated Priority: 1
Q-values before update: [[1.0199363 0.8792933]]
Q-values after update: [[1.0268831 0.8842104]]
Designated Priority: 1
Q-values before update: [[1.0359404 0.8917424]]
Q-values after update: [[1.0414935  0.89605135]]
Designated Priority: 1
Q-values before update: [[1.0512767  0.90439516]]
Q-values after update: [[1.0552524 0.9080087]]
Designated Priority: 1
Q-values before update: [[1.0657539 0.9169518]]
Q-values after update: [[1.0683167 0.9199369]]
Designated Priority: 1
Q-values before update: [[1.0788088 0.9290631]]
Q-values after update: [[1.0798223 0.9313328]]
Designated Priority: 1
Q-values before update: [[1.0901943  0.94064593]]
Q-values after update: [[1.0896442  0.94216377]]
Designated Priority: 1
Q-values before update: [[1.0998534  0.95156145]]
Q-values after update: [[1.0977702 0.9522873]]
Designated Priority: 1
Q-values before update: [[1.1076579 0.9616071]]
Q-values after update: [[1.1041439  0.96153295]]
Designated Priority: 1
Q-values before update: [[1.1135622 0.9715208]]
Q-values after update: [[1.1087141  0.97051716]]
Designated Priority: 1
Q-values before update: [[1.1110649 0.9765129]]
Q-values after update: [[1.1101596 0.9810029]]
Designated Priority: 1
Q-values before update: [[1.1000255 0.9725822]]
Q-values after update: [[1.0975108 0.9755062]]
Designated Priority: 1
Q-values before update: [[1.091893  0.9764495]]
Q-values after update: [[1.0900955  0.97939646]]
Designated Priority: 1
Q-values before update: [[1.0828776  0.97951627]]
Q-values after update: [[1.0828235 0.9830695]]
Designated Priority: 3
Q-values before update: [[1.0728518 0.9833378]]
Q-values after update: [[1.0466094 0.9715123]]
Episode 73 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [-0.18688165 -1.912569    0.25598264  2.9779994 ], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[1.0178446 0.9206691]]
Q-values after update: [[1.0061167  0.91828704]]
Designated Priority: 1
Q-values before update: [[1.0156295 0.9266223]]
Q-values after update: [[1.0045093 0.9239057]]
Designated Priority: 1
Q-values before update: [[1.0132662 0.9318001]]
Q-values after update: [[1.0032978  0.92907065]]
Designated Priority: 1
Q-values before update: [[1.0108802  0.93619967]]
Q-values after update: [[1.0025187 0.9364042]]
Designated Priority: 1
Q-values before update: [[0.9930854 0.9288912]]
Q-values after update: [[0.9874221 0.9299183]]
Designated Priority: 1
Q-values before update: [[0.9940469  0.93630075]]
Q-values after update: [[0.99025935 0.93762636]]
Designated Priority: 1
Q-values before update: [[0.9959044 0.9438889]]
Q-values after update: [[0.9943291  0.94578993]]
Designated Priority: 1
Q-values before update: [[0.9930768  0.94849944]]
Q-values after update: [[0.9939674 0.9511473]]
Designated Priority: 1
Q-values before update: [[0.9810791  0.94588476]]
Q-values after update: [[0.9863608 0.950611 ]]
Designated Priority: 3
Q-values before update: [[0.97188056 0.9444953 ]]
Q-values after update: [[0.9839857 0.9531548]]
Episode 74 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.16307792 -1.577518    0.22154595  2.5463543 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.9907436  0.93201417]]
Q-values after update: [[0.9981822 0.9366618]]
Designated Priority: 1
Q-values before update: [[1.0056622  0.94356763]]
Q-values after update: [[1.0129924 0.9481772]]
Designated Priority: 1
Q-values before update: [[1.0203846  0.95526016]]
Q-values after update: [[1.027422  0.9597385]]
Designated Priority: 1
Q-values before update: [[1.0346763 0.9669602]]
Q-values after update: [[1.0413134  0.97124803]]
Designated Priority: 1
Q-values before update: [[1.0485365  0.97878647]]
Q-values after update: [[1.0546858 0.9828285]]
Designated Priority: 1
Q-values before update: [[1.0616279 0.9909462]]
Q-values after update: [[1.0672383 0.9947012]]
Designated Priority: 1
Q-values before update: [[1.0714226 1.0017946]]
Q-values after update: [[1.0769415 1.0055647]]
Designated Priority: 1
Q-values before update: [[1.0669322 1.0029373]]
Q-values after update: [[1.0727719 1.0069224]]
Designated Priority: 1
Q-values before update: [[1.0582926 1.0051246]]
Q-values after update: [[1.065839 1.010097]]
Designated Priority: 3
Q-values before update: [[1.0500703 1.0077194]]
Q-values after update: [[1.0387504 1.0015275]]
Episode 75 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.12167257 -1.905774    0.2267014   3.0506294 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.034162  0.9643436]]
Q-values after update: [[1.0300924 0.9633534]]
Designated Priority: 1
Q-values before update: [[1.0388398 0.9714649]]
Q-values after update: [[1.0350727  0.97119004]]
Designated Priority: 1
Q-values before update: [[1.0261655  0.96326494]]
Q-values after update: [[1.0228425 0.9632015]]
Designated Priority: 1
Q-values before update: [[1.0307429 0.9706466]]
Q-values after update: [[1.0272542  0.97025144]]
Designated Priority: 1
Q-values before update: [[1.0344994  0.97736675]]
Q-values after update: [[1.0311236  0.97678816]]
Designated Priority: 1
Q-values before update: [[1.0376134  0.98346174]]
Q-values after update: [[1.0346401 0.9828584]]
Designated Priority: 1
Q-values before update: [[1.0404066 0.9891341]]
Q-values after update: [[1.0381587 0.9886935]]
Designated Priority: 1
Q-values before update: [[1.0430833 0.9950608]]
Q-values after update: [[1.0419184  0.99501026]]
Designated Priority: 1
Q-values before update: [[1.0334457  0.99281263]]
Q-values after update: [[1.034088   0.99354386]]
Designated Priority: 1
Q-values before update: [[1.0162671  0.98853624]]
Q-values after update: [[1.0208082  0.99147975]]
Designated Priority: 1
Q-values before update: [[1.0008922 0.9858339]]
Q-values after update: [[1.0118358 0.9925066]]
Designated Priority: 3
Q-values before update: [[0.9906901 0.9863592]]
Q-values after update: [[1.0046866 0.9949939]]
Episode 76 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.18918955 -1.9711388   0.2606652   3.1015203 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.031325   0.97085255]]
Q-values after update: [[1.0368172 0.9734125]]
Designated Priority: 1
Q-values before update: [[1.0450408  0.98107934]]
Q-values after update: [[1.0506538  0.98436797]]
Designated Priority: 1
Q-values before update: [[1.0410256 0.9758259]]
Q-values after update: [[1.0446155 0.9780277]]
Designated Priority: 1
Q-values before update: [[1.0537229  0.98645175]]
Q-values after update: [[1.0561423 0.9882742]]
Designated Priority: 1
Q-values before update: [[1.0651437  0.99680567]]
Q-values after update: [[1.0663772 0.9981978]]
Designated Priority: 1
Q-values before update: [[1.0751839 1.0068276]]
Q-values after update: [[1.0752457 1.0077407]]
Designated Priority: 1
Q-values before update: [[1.0838277 1.0164323]]
Q-values after update: [[1.0827688 1.0168289]]
Designated Priority: 1
Q-values before update: [[1.0910282 1.0257717]]
Q-values after update: [[1.0889556 1.0256298]]
Designated Priority: 1
Q-values before update: [[1.0959755 1.0349472]]
Q-values after update: [[1.0933965 1.0345432]]
Designated Priority: 1
Q-values before update: [[1.0832012 1.0330873]]
Q-values after update: [[1.08107   1.0327723]]
Designated Priority: 1
Q-values before update: [[1.067174  1.0315919]]
Q-values after update: [[1.0671718 1.0324143]]
Designated Priority: 3
Q-values before update: [[1.0518813 1.0305547]]
Q-values after update: [[1.0329016 1.0197651]]
Episode 77 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.14993471 -1.9097055   0.23570679  3.0414984 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.0263408 0.9748399]]
Q-values after update: [[1.0174727 0.9715673]]
Designated Priority: 1
Q-values before update: [[1.0262619  0.97996604]]
Q-values after update: [[1.0175871  0.97647077]]
Designated Priority: 1
Q-values before update: [[1.0253165 0.9842313]]
Q-values after update: [[1.0172552 0.9807446]]
Designated Priority: 1
Q-values before update: [[1.0240748 0.9879219]]
Q-values after update: [[1.0170585 0.9846969]]
Designated Priority: 1
Q-values before update: [[1.0230538  0.99144787]]
Q-values after update: [[1.0175016  0.98872447]]
Designated Priority: 1
Q-values before update: [[1.022676  0.9949546]]
Q-values after update: [[1.0182927  0.99441373]]
Designated Priority: 1
Q-values before update: [[1.0091915  0.98694277]]
Q-values after update: [[1.0070689  0.98731273]]
Designated Priority: 1
Q-values before update: [[1.0113025  0.99298584]]
Q-values after update: [[1.0110431  0.99401915]]
Designated Priority: 1
Q-values before update: [[0.99723417 0.98830557]]
Q-values after update: [[1.0005033 0.9911416]]
Designated Priority: 1
Q-values before update: [[0.9816994 0.9858971]]
Q-values after update: [[0.9872899  0.99342525]]
Designated Priority: 3
Q-values before update: [[0.98535365 0.9871819 ]]
Q-values after update: [[0.9918983 0.9971005]]
Episode 78 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.13092782 -1.0294807   0.23845357  1.6522709 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[0.99986386 0.97985697]]
Q-values after update: [[1.0034825 0.9865989]]
Designated Priority: 1
Q-values before update: [[0.99640125 0.979147  ]]
Q-values after update: [[0.99943316 0.98488253]]
Designated Priority: 1
Q-values before update: [[1.0069207  0.99264115]]
Q-values after update: [[1.01009    0.99859273]]
Designated Priority: 1
Q-values before update: [[1.0024583  0.99040914]]
Q-values after update: [[1.0049694 0.9954211]]
Designated Priority: 1
Q-values before update: [[1.0129797 1.0038687]]
Q-values after update: [[1.0155108 1.0087544]]
Designated Priority: 1
Q-values before update: [[1.0074394 0.9998045]]
Q-values after update: [[1.0092963 1.0038536]]
Designated Priority: 1
Q-values before update: [[1.0177295 1.0130364]]
Q-values after update: [[1.0192229 1.0167873]]
Designated Priority: 1
Q-values before update: [[1.0279565 1.0262012]]
Q-values after update: [[1.0292375 1.0297074]]
Designated Priority: 1
Q-values before update: [[1.0376666 1.0391872]]
Q-values after update: [[1.0385331 1.0413245]]
Designated Priority: 1
Q-values before update: [[1.0282722 1.0310514]]
Q-values after update: [[1.0286009 1.031827 ]]
Designated Priority: 1
Q-values before update: [[1.0188022 1.0216457]]
Q-values after update: [[1.0186974 1.0221058]]
Designated Priority: 1
Q-values before update: [[1.0280995 1.0322695]]
Q-values after update: [[1.0277452 1.031791 ]]
Designated Priority: 1
Q-values before update: [[1.0179077 1.0214937]]
Q-values after update: [[1.0172843 1.0208926]]
Designated Priority: 1
Q-values before update: [[1.0268021 1.0312119]]
Q-values after update: [[1.025991 1.029841]]
Designated Priority: 1
Q-values before update: [[1.0162017 1.0195001]]
Q-values after update: [[1.0153878 1.0180838]]
Designated Priority: 1
Q-values before update: [[1.0069289 1.007875 ]]
Q-values after update: [[1.006335  1.0070622]]
Designated Priority: 1
Q-values before update: [[0.99834776 0.99694777]]
Q-values after update: [[0.9983396  0.99642444]]
Designated Priority: 1
Q-values before update: [[1.0079446 1.0068437]]
Q-values after update: [[1.00794   1.0063766]]
Designated Priority: 1
Q-values before update: [[1.0171442 1.0167717]]
Q-values after update: [[1.0169485 1.0162826]]
Designated Priority: 1
Q-values before update: [[1.0263196 1.0269591]]
Q-values after update: [[1.025937  1.0259125]]
Designated Priority: 1
Q-values before update: [[1.0163519 1.0151565]]
Q-values after update: [[1.0159844 1.014206 ]]
Designated Priority: 1
Q-values before update: [[1.0252101 1.024806 ]]
Q-values after update: [[1.0248008 1.0239167]]
Designated Priority: 1
Q-values before update: [[1.034203  1.0348077]]
Q-values after update: [[1.0335745 1.0332482]]
Designated Priority: 1
Q-values before update: [[1.0230488 1.0221742]]
Q-values after update: [[1.0223837 1.0204846]]
Designated Priority: 1
Q-values before update: [[1.0134928 1.0101885]]
Q-values after update: [[1.0129267 1.0086987]]
Designated Priority: 1
Q-values before update: [[1.0219455 1.0191618]]
Q-values after update: [[1.0214231 1.0178018]]
Designated Priority: 1
Q-values before update: [[1.0308164 1.0286574]]
Q-values after update: [[1.0301459 1.0268917]]
Designated Priority: 1
Q-values before update: [[1.0202346 1.0162575]]
Q-values after update: [[1.0195742 1.0146681]]
Designated Priority: 1
Q-values before update: [[1.0287702 1.0253906]]
Q-values after update: [[1.0280316 1.0235865]]
Designated Priority: 1
Q-values before update: [[1.0185326 1.0132405]]
Q-values after update: [[1.0177968 1.0116107]]
Designated Priority: 1
Q-values before update: [[1.0267217 1.0221679]]
Q-values after update: [[1.026537 1.020881]]
Designated Priority: 1
Q-values before update: [[1.0357778 1.0318801]]
Q-values after update: [[1.036454  1.0310707]]
Designated Priority: 1
Q-values before update: [[1.0453569 1.0418243]]
Q-values after update: [[1.0474001 1.0417321]]
Designated Priority: 1
Q-values before update: [[1.0559871 1.0522519]]
Q-values after update: [[1.0597858 1.0530877]]
Designated Priority: 1
Q-values before update: [[1.0681716 1.0636151]]
Q-values after update: [[1.0739204 1.065531 ]]
Designated Priority: 1
Q-values before update: [[1.0822061 1.0761418]]
Q-values after update: [[1.0900154 1.0792661]]
Designated Priority: 1
Q-values before update: [[1.0947571 1.0915332]]
Q-values after update: [[1.1048621 1.0960054]]
Designated Priority: 1
Q-values before update: [[1.1017965 1.1031115]]
Q-values after update: [[1.1125214 1.1097659]]
Designated Priority: 1
Q-values before update: [[1.1082944 1.1006103]]
Q-values after update: [[1.1201725 1.1076696]]
Designated Priority: 1
Q-values before update: [[1.1087661 1.110162 ]]
Q-values after update: [[1.1212174 1.1191323]]
Designated Priority: 1
Q-values before update: [[1.1153438 1.1085434]]
Q-values after update: [[1.1286131 1.1176157]]
Designated Priority: 3
Q-values before update: [[1.1175393 1.1215487]]
Q-values after update: [[1.1035097 1.0844755]]
Episode 79 out of total 100, Total Reward: 42.0, Epsilon: 0.75, Current State: [-0.2942633 -1.5240225  0.2236284  1.8562355], Steps Taken: 42
Designated Priority: 1
Q-values before update: [[1.0586302 0.9987474]]
Q-values after update: [[1.0555594  0.98087204]]
Designated Priority: 1
Q-values before update: [[1.0664927 0.991109 ]]
Q-values after update: [[1.0614022 0.9735377]]
Designated Priority: 1
Q-values before update: [[1.0709821 0.9823983]]
Q-values after update: [[1.0643067 0.9652859]]
Designated Priority: 1
Q-values before update: [[1.0726514 0.9730545]]
Q-values after update: [[1.0649085 0.956602 ]]
Designated Priority: 1
Q-values before update: [[1.0719179 0.9631692]]
Q-values after update: [[1.0654179 0.9502914]]
Designated Priority: 1
Q-values before update: [[1.0549309 0.942545 ]]
Q-values after update: [[1.049146  0.9314536]]
Designated Priority: 1
Q-values before update: [[1.0550568 0.9366281]]
Q-values after update: [[1.049304   0.92619056]]
Designated Priority: 1
Q-values before update: [[1.0468272 0.9254311]]
Q-values after update: [[1.0410912  0.91540825]]
Designated Priority: 1
Q-values before update: [[1.025072  0.9061518]]
Q-values after update: [[1.0217361 0.8978034]]
Designated Priority: 3
Q-values before update: [[1.0011159 0.8876271]]
Q-values after update: [[0.9976186  0.87956214]]
Episode 80 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.09975643 -1.614372    0.21249598  2.5216954 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0214298 0.8920064]]
Q-values after update: [[1.0203373  0.88716626]]
Designated Priority: 1
Q-values before update: [[1.0256099 0.8908065]]
Q-values after update: [[1.0247084 0.8863452]]
Designated Priority: 1
Q-values before update: [[1.0297111  0.88977474]]
Q-values after update: [[1.02911  0.885707]]
Designated Priority: 1
Q-values before update: [[1.0334408 0.8887007]]
Q-values after update: [[1.0334194 0.8851397]]
Designated Priority: 1
Q-values before update: [[1.0370243 0.8876109]]
Q-values after update: [[1.0378399 0.884679 ]]
Designated Priority: 1
Q-values before update: [[1.0351427  0.88293576]]
Q-values after update: [[1.0372506 0.8808284]]
Designated Priority: 1
Q-values before update: [[1.0198087 0.8691107]]
Q-values after update: [[1.0247903 0.8687111]]
Designated Priority: 1
Q-values before update: [[1.0045923 0.8565451]]
Q-values after update: [[1.0144932 0.8588501]]
Designated Priority: 3
Q-values before update: [[0.98943883 0.84640276]]
Q-values after update: [[1.0021492 0.8505317]]
Episode 81 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.1917962  -1.8059021   0.23997805  2.8026702 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0392351 0.8678255]]
Q-values after update: [[1.0445167  0.86806417]]
Designated Priority: 1
Q-values before update: [[1.0510975 0.8718792]]
Q-values after update: [[1.0550865 0.8719251]]
Designated Priority: 1
Q-values before update: [[1.0615871  0.87579226]]
Q-values after update: [[1.0642016 0.8755515]]
Designated Priority: 1
Q-values before update: [[1.0703793 0.8794267]]
Q-values after update: [[1.0716552 0.8788469]]
Designated Priority: 1
Q-values before update: [[1.0773709 0.8824862]]
Q-values after update: [[1.0773994 0.8815398]]
Designated Priority: 1
Q-values before update: [[1.0807219  0.88382053]]
Q-values after update: [[1.0801677 0.8828727]]
Designated Priority: 1
Q-values before update: [[1.0658365 0.8733305]]
Q-values after update: [[1.0653254 0.8724235]]
Designated Priority: 1
Q-values before update: [[1.0493162 0.862839 ]]
Q-values after update: [[1.0543314 0.8702682]]
Designated Priority: 3
Q-values before update: [[1.0456896 0.8650694]]
Q-values after update: [[1.0660605  0.89734244]]
Episode 82 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.0889153  -0.94970495  0.2364822   1.711142  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.058854  0.8893049]]
Q-values after update: [[1.0639045 0.9077835]]
Designated Priority: 1
Q-values before update: [[1.0746056  0.91541314]]
Q-values after update: [[1.078366  0.9327394]]
Designated Priority: 1
Q-values before update: [[1.0896207  0.94132876]]
Q-values after update: [[1.0918272 0.9573677]]
Designated Priority: 1
Q-values before update: [[1.1034302 0.9667603]]
Q-values after update: [[1.1038115 0.9813359]]
Designated Priority: 1
Q-values before update: [[1.1156343  0.99137795]]
Q-values after update: [[1.1139439 1.0042982]]
Designated Priority: 1
Q-values before update: [[1.1258761 1.0148969]]
Q-values after update: [[1.1219205 1.0259705]]
Designated Priority: 1
Q-values before update: [[1.1337949 1.0371059]]
Q-values after update: [[1.1274471 1.0462368]]
Designated Priority: 1
Q-values before update: [[1.1339686 1.0548083]]
Q-values after update: [[1.1267952 1.0628587]]
Designated Priority: 1
Q-values before update: [[1.1221726 1.0638618]]
Q-values after update: [[1.1140764 1.0704339]]
Designated Priority: 3
Q-values before update: [[1.1052991 1.0714592]]
Q-values after update: [[1.0830768 1.0535874]]
Episode 83 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.1265241  -1.5334103   0.25003943  2.4749827 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0253404  0.98072034]]
Q-values after update: [[1.0140432 0.9731507]]
Designated Priority: 1
Q-values before update: [[1.0259173 0.9840585]]
Q-values after update: [[1.0149622  0.97652376]]
Designated Priority: 1
Q-values before update: [[1.0256419 0.9866038]]
Q-values after update: [[1.015445  0.9793346]]
Designated Priority: 1
Q-values before update: [[1.0250248 0.9885191]]
Q-values after update: [[1.0159931 0.9817416]]
Designated Priority: 1
Q-values before update: [[1.0245646  0.99016494]]
Q-values after update: [[1.0171014  0.98411286]]
Designated Priority: 1
Q-values before update: [[1.0248008  0.99189615]]
Q-values after update: [[1.0192983 0.9868161]]
Designated Priority: 1
Q-values before update: [[1.0262173 0.9941378]]
Q-values after update: [[1.0230956 0.9902904]]
Designated Priority: 1
Q-values before update: [[1.0197282 0.9906004]]
Q-values after update: [[1.0197906 0.9884974]]
Designated Priority: 1
Q-values before update: [[1.0089698 0.983552 ]]
Q-values after update: [[1.0142016  0.98439634]]
Designated Priority: 3
Q-values before update: [[0.9996016  0.97910213]]
Q-values after update: [[1.0046993 0.9800636]]
Episode 84 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.15628645 -2.003539    0.2516022   3.1100454 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.9824438  0.94310063]]
Q-values after update: [[0.9855095 0.9431385]]
Designated Priority: 1
Q-values before update: [[0.99463797 0.95101964]]
Q-values after update: [[0.9981444 0.951348 ]]
Designated Priority: 1
Q-values before update: [[1.0070798  0.95918787]]
Q-values after update: [[1.0109733  0.95978355]]
Designated Priority: 1
Q-values before update: [[1.0196598 0.9675475]]
Q-values after update: [[1.0239084  0.96839964]]
Designated Priority: 1
Q-values before update: [[1.0323341 0.9760525]]
Q-values after update: [[1.0369143 0.9771576]]
Designated Priority: 1
Q-values before update: [[1.045116  0.9847356]]
Q-values after update: [[1.0503447  0.98785055]]
Designated Priority: 1
Q-values before update: [[1.0373589 0.9776433]]
Q-values after update: [[1.0423521  0.98050284]]
Designated Priority: 1
Q-values before update: [[1.051334  0.9887054]]
Q-values after update: [[1.056478  0.9916377]]
Designated Priority: 1
Q-values before update: [[1.0652761 0.9998425]]
Q-values after update: [[1.0704923 1.0028113]]
Designated Priority: 1
Q-values before update: [[1.0724115 1.0067692]]
Q-values after update: [[1.0781418 1.0100719]]
Designated Priority: 3
Q-values before update: [[1.070256  1.0068827]]
Q-values after update: [[1.0744805 1.0081964]]
Episode 85 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.1331831  -1.3351916   0.21200788  2.1478887 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0180199 0.953224 ]]
Q-values after update: [[1.0204405  0.95372075]]
Designated Priority: 1
Q-values before update: [[1.0321257  0.96334565]]
Q-values after update: [[1.0338943  0.96365815]]
Designated Priority: 1
Q-values before update: [[1.0451761  0.97307944]]
Q-values after update: [[1.0461911  0.97314346]]
Designated Priority: 1
Q-values before update: [[1.0571238  0.98249304]]
Q-values after update: [[1.0585477  0.98363346]]
Designated Priority: 1
Q-values before update: [[1.0452986 0.973212 ]]
Q-values after update: [[1.0458239 0.9739071]]
Designated Priority: 1
Q-values before update: [[1.0570415 0.9834348]]
Q-values after update: [[1.0567925 0.9837767]]
Designated Priority: 1
Q-values before update: [[1.067618   0.99320483]]
Q-values after update: [[1.0679708  0.99474275]]
Designated Priority: 1
Q-values before update: [[1.0543666 0.984184 ]]
Q-values after update: [[1.054016  0.9852469]]
Designated Priority: 1
Q-values before update: [[1.0650868 0.994864 ]]
Q-values after update: [[1.0641108 0.9955489]]
Designated Priority: 1
Q-values before update: [[1.0743855 1.0055716]]
Q-values after update: [[1.0728037 1.0058582]]
Designated Priority: 3
Q-values before update: [[1.0682459 1.0049458]]
Q-values after update: [[1.0661347 1.0040255]]
Episode 86 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.11035823 -0.9680839   0.24513346  1.8090316 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0207717 0.9596569]]
Q-values after update: [[1.0190794  0.95915914]]
Designated Priority: 1
Q-values before update: [[1.0308244  0.96892935]]
Q-values after update: [[1.0289121 0.9683063]]
Designated Priority: 1
Q-values before update: [[1.0401982 0.9777914]]
Q-values after update: [[1.0388181  0.97819114]]
Designated Priority: 1
Q-values before update: [[1.0261282 0.9680095]]
Q-values after update: [[1.0247383  0.96831155]]
Designated Priority: 1
Q-values before update: [[1.0360707  0.97786295]]
Q-values after update: [[1.0346081 0.978047 ]]
Designated Priority: 1
Q-values before update: [[1.0453886  0.98731786]]
Q-values after update: [[1.043894   0.98740447]]
Designated Priority: 1
Q-values before update: [[1.0542295 0.9965488]]
Q-values after update: [[1.052763  0.9965674]]
Designated Priority: 1
Q-values before update: [[1.0626009 1.0054669]]
Q-values after update: [[1.0612476 1.0054625]]
Designated Priority: 1
Q-values before update: [[1.0703635 1.0143906]]
Q-values after update: [[1.0692978 1.0144552]]
Designated Priority: 1
Q-values before update: [[1.0633378 1.0123109]]
Q-values after update: [[1.0636007 1.0130323]]
Designated Priority: 3
Q-values before update: [[1.0555552 1.0095216]]
Q-values after update: [[1.0392097 1.0003786]]
Episode 87 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.15809149 -1.7444485   0.25214148  2.8671243 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0035576 0.9609053]]
Q-values after update: [[0.9965402 0.9585401]]
Designated Priority: 1
Q-values before update: [[1.0063077 0.9668709]]
Q-values after update: [[1.0001136  0.96455884]]
Designated Priority: 1
Q-values before update: [[1.0090513 0.9723116]]
Q-values after update: [[1.004002  0.9702509]]
Designated Priority: 1
Q-values before update: [[1.0120038  0.97741187]]
Q-values after update: [[1.0083579 0.9757723]]
Designated Priority: 1
Q-values before update: [[1.0155879 0.9824779]]
Q-values after update: [[1.0136155 0.9814506]]
Designated Priority: 1
Q-values before update: [[1.020117  0.9876738]]
Q-values after update: [[1.0201031  0.98747444]]
Designated Priority: 1
Q-values before update: [[1.0259603  0.99330795]]
Q-values after update: [[1.0282053  0.99418163]]
Designated Priority: 1
Q-values before update: [[1.0215366  0.99089074]]
Q-values after update: [[1.0265759 0.9931771]]
Designated Priority: 1
Q-values before update: [[1.0139446 0.9856579]]
Q-values after update: [[1.0239468 0.9909286]]
Designated Priority: 3
Q-values before update: [[1.009927  0.9825892]]
Q-values after update: [[1.0161486  0.98569775]]
Episode 88 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.21144997 -1.9662642   0.24210434  3.0559719 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.99696654 0.95798045]]
Q-values after update: [[1.0017402 0.959882 ]]
Designated Priority: 1
Q-values before update: [[1.010689  0.9675946]]
Q-values after update: [[1.015655   0.96962535]]
Designated Priority: 1
Q-values before update: [[1.0247117  0.97742504]]
Q-values after update: [[1.0297368  0.97952557]]
Designated Priority: 1
Q-values before update: [[1.038425  0.9871479]]
Q-values after update: [[1.0434228  0.98928225]]
Designated Priority: 1
Q-values before update: [[1.0518163 0.9968208]]
Q-values after update: [[1.0567268 0.9989648]]
Designated Priority: 1
Q-values before update: [[1.0647295 1.0063163]]
Q-values after update: [[1.0695114 1.0084513]]
Designated Priority: 1
Q-values before update: [[1.0724761 1.0122328]]
Q-values after update: [[1.0773743 1.0144932]]
Designated Priority: 1
Q-values before update: [[1.0670422 1.008884 ]]
Q-values after update: [[1.0730715 1.011867 ]]
Designated Priority: 3
Q-values before update: [[1.0611756 1.0052897]]
Q-values after update: [[1.0658162 1.0066464]]
Episode 89 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.17155334 -1.3852586   0.2442591   2.2339718 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0425385 0.9761377]]
Q-values after update: [[1.0447003 0.9763551]]
Designated Priority: 1
Q-values before update: [[1.0551302 0.9849056]]
Q-values after update: [[1.0559176  0.98466206]]
Designated Priority: 1
Q-values before update: [[1.0659281  0.99304605]]
Q-values after update: [[1.0653824 0.9923264]]
Designated Priority: 1
Q-values before update: [[1.0749009 1.0004721]]
Q-values after update: [[1.0731119  0.99927163]]
Designated Priority: 1
Q-values before update: [[1.0820893 1.0071144]]
Q-values after update: [[1.0791972 1.0054476]]
Designated Priority: 1
Q-values before update: [[1.0876155 1.0129782]]
Q-values after update: [[1.0838209 1.010892 ]]
Designated Priority: 1
Q-values before update: [[1.0916595 1.0180974]]
Q-values after update: [[1.087234  1.0156837]]
Designated Priority: 1
Q-values before update: [[1.0817419 1.0134624]]
Q-values after update: [[1.0776875 1.0112052]]
Designated Priority: 1
Q-values before update: [[1.0661936 1.0046601]]
Q-values after update: [[1.064059  1.0034713]]
Designated Priority: 3
Q-values before update: [[1.050523   0.99580026]]
Q-values after update: [[1.0311348 0.9843298]]
Episode 90 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.13392872 -1.9357321   0.24053842  3.0860677 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0167012  0.96156263]]
Q-values after update: [[1.0080708 0.9579361]]
Designated Priority: 1
Q-values before update: [[1.0164955 0.9649729]]
Q-values after update: [[1.0081531 0.961211 ]]
Designated Priority: 1
Q-values before update: [[1.0156814 0.9676153]]
Q-values after update: [[1.0080965 0.9639727]]
Designated Priority: 1
Q-values before update: [[1.0145957  0.96971357]]
Q-values after update: [[1.0081563  0.96640515]]
Designated Priority: 1
Q-values before update: [[1.0136496  0.97145915]]
Q-values after update: [[1.0087533 0.9687209]]
Designated Priority: 1
Q-values before update: [[1.0133396 0.9731668]]
Q-values after update: [[1.010403  0.9712677]]
Designated Priority: 1
Q-values before update: [[1.005015  0.9683081]]
Q-values after update: [[1.0044451 0.9674492]]
Designated Priority: 1
Q-values before update: [[0.98883057 0.95711535]]
Q-values after update: [[0.99277365 0.9587971 ]]
Designated Priority: 3
Q-values before update: [[0.9740484 0.9473598]]
Q-values after update: [[0.9848772 0.953218 ]]
Episode 91 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.12572235 -1.77892     0.22186056  2.814864  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[0.99610424 0.95216405]]
Q-values after update: [[1.0019889 0.9542309]]
Designated Priority: 1
Q-values before update: [[1.0089529 0.9599858]]
Q-values after update: [[1.01495   0.9622485]]
Designated Priority: 1
Q-values before update: [[1.0220535 0.9682305]]
Q-values after update: [[1.0280318  0.97060895]]
Designated Priority: 1
Q-values before update: [[1.0349534  0.97658193]]
Q-values after update: [[1.040869   0.97904265]]
Designated Priority: 1
Q-values before update: [[1.0475817  0.98494446]]
Q-values after update: [[1.0539196 0.9890274]]
Designated Priority: 1
Q-values before update: [[1.0428557 0.980473 ]]
Q-values after update: [[1.048324   0.98393244]]
Designated Priority: 1
Q-values before update: [[1.0558343 0.9904978]]
Q-values after update: [[1.0610178 0.993832 ]]
Designated Priority: 1
Q-values before update: [[1.068253  1.0003167]]
Q-values after update: [[1.0730942 1.0034889]]
Designated Priority: 1
Q-values before update: [[1.0800442 1.0098865]]
Q-values after update: [[1.084521  1.0128744]]
Designated Priority: 1
Q-values before update: [[1.078886  1.0100203]]
Q-values after update: [[1.083975  1.0134133]]
Designated Priority: 1
Q-values before update: [[1.0715728 1.0060651]]
Q-values after update: [[1.0781558 1.010351 ]]
Designated Priority: 3
Q-values before update: [[1.0613971 1.0022776]]
Q-values after update: [[1.0462534  0.99366546]]
Episode 92 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.16685672 -1.9254762   0.24607803  2.997863  ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.0398302  0.97627974]]
Q-values after update: [[1.0338767 0.9743737]]
Designated Priority: 1
Q-values before update: [[1.0424386  0.98140705]]
Q-values after update: [[1.0361593  0.97911054]]
Designated Priority: 1
Q-values before update: [[1.0437813 0.9854875]]
Q-values after update: [[1.037586  0.9830117]]
Designated Priority: 1
Q-values before update: [[1.0441685  0.98869693]]
Q-values after update: [[1.0384475 0.9862431]]
Designated Priority: 1
Q-values before update: [[1.0441331  0.99140525]]
Q-values after update: [[1.0394015 0.9906776]]
Designated Priority: 1
Q-values before update: [[1.0298679 0.9832753]]
Q-values after update: [[1.0266471  0.98313844]]
Designated Priority: 1
Q-values before update: [[1.0317976  0.98785007]]
Q-values after update: [[1.0297556 0.9880227]]
Designated Priority: 1
Q-values before update: [[1.0342102 0.9923234]]
Q-values after update: [[1.0336871  0.99303603]]
Designated Priority: 1
Q-values before update: [[1.0311195 0.992038 ]]
Q-values after update: [[1.0324519  0.99346566]]
Designated Priority: 1
Q-values before update: [[1.0158596 0.9823959]]
Q-values after update: [[1.021068 0.985968]]
Designated Priority: 1
Q-values before update: [[0.99902874 0.9738311 ]]
Q-values after update: [[1.0105695 0.9810781]]
Designated Priority: 3
Q-values before update: [[0.9869939  0.96801716]]
Q-values after update: [[1.0024774  0.97777367]]
Episode 93 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.23232672 -1.9352683   0.26257294  3.0536902 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.0300884  0.98222667]]
Q-values after update: [[1.0369636  0.98559225]]
Designated Priority: 1
Q-values before update: [[1.0451062  0.99234885]]
Q-values after update: [[1.0512458 0.9955596]]
Designated Priority: 1
Q-values before update: [[1.0592244 1.002322 ]]
Q-values after update: [[1.0644896 1.0052768]]
Designated Priority: 1
Q-values before update: [[1.0722817 1.0120296]]
Q-values after update: [[1.0765946 1.014653 ]]
Designated Priority: 1
Q-values before update: [[1.0842804 1.021471 ]]
Q-values after update: [[1.0875851 1.0236913]]
Designated Priority: 1
Q-values before update: [[1.0950296 1.0304744]]
Q-values after update: [[1.0986674 1.0335221]]
Designated Priority: 1
Q-values before update: [[1.0857158 1.0233904]]
Q-values after update: [[1.0878754 1.0255306]]
Designated Priority: 1
Q-values before update: [[1.0960379 1.0329133]]
Q-values after update: [[1.0972688 1.034581 ]]
Designated Priority: 1
Q-values before update: [[1.1012436 1.0390472]]
Q-values after update: [[1.1021792 1.040605 ]]
Designated Priority: 1
Q-values before update: [[1.0908402 1.0339576]]
Q-values after update: [[1.0922416 1.0357224]]
Designated Priority: 3
Q-values before update: [[1.0775666 1.0280935]]
Q-values after update: [[1.0541589 1.015058 ]]
Episode 94 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.20329183 -1.7171044   0.2380981   2.7654912 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.0396073  0.99088836]]
Q-values after update: [[1.0283113  0.98673236]]
Designated Priority: 1
Q-values before update: [[1.037123  0.9942745]]
Q-values after update: [[1.0259277 0.9897804]]
Designated Priority: 1
Q-values before update: [[1.0334003 0.9963404]]
Q-values after update: [[1.022859  0.9918153]]
Designated Priority: 1
Q-values before update: [[1.0290651 0.9974439]]
Q-values after update: [[1.019661  0.9931593]]
Designated Priority: 1
Q-values before update: [[1.0247059  0.99799293]]
Q-values after update: [[1.016947   0.99425066]]
Designated Priority: 1
Q-values before update: [[1.0202556 0.9977859]]
Q-values after update: [[1.014005   0.99438393]]
Designated Priority: 1
Q-values before update: [[0.99776745 0.98290324]]
Q-values after update: [[0.9954163  0.98150516]]
Designated Priority: 3
Q-values before update: [[0.9734466 0.968588 ]]
Q-values after update: [[0.97759354 0.9709922 ]]
Episode 95 out of total 100, Total Reward: 8.0, Epsilon: 0.75, Current State: [-0.14766322 -1.6030033   0.21531743  2.5263133 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[1.0016594 0.981279 ]]
Q-values after update: [[1.0044976  0.98249745]]
Designated Priority: 1
Q-values before update: [[1.0104228 0.9875213]]
Q-values after update: [[1.0135901 0.9889102]]
Designated Priority: 1
Q-values before update: [[1.0190187 0.9936466]]
Q-values after update: [[1.0225737 0.9952286]]
Designated Priority: 1
Q-values before update: [[1.0275252  0.99969155]]
Q-values after update: [[1.0312403 1.0021961]]
Designated Priority: 1
Q-values before update: [[1.022739  0.9953463]]
Q-values after update: [[1.0264754 0.9977067]]
Designated Priority: 1
Q-values before update: [[1.0317988 1.0025108]]
Q-values after update: [[1.0358987 1.0050035]]
Designated Priority: 1
Q-values before update: [[1.0408108 1.0095763]]
Q-values after update: [[1.0453635 1.0122592]]
Designated Priority: 1
Q-values before update: [[1.0498502 1.0166594]]
Q-values after update: [[1.0547681 1.0206606]]
Designated Priority: 1
Q-values before update: [[1.0443771 1.0124948]]
Q-values after update: [[1.0493674 1.0162823]]
Designated Priority: 1
Q-values before update: [[1.0542889 1.0210438]]
Q-values after update: [[1.0598267 1.0250431]]
Designated Priority: 1
Q-values before update: [[1.0513004 1.0198466]]
Q-values after update: [[1.0583677 1.0246941]]
Designated Priority: 1
Q-values before update: [[1.0400609 1.0139391]]
Q-values after update: [[1.050038  1.0204698]]
Designated Priority: 3
Q-values before update: [[1.0283244 1.0087901]]
Q-values after update: [[1.0287404 1.0096065]]
Episode 96 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [-0.22127795 -1.7249365   0.24767645  2.802449  ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[1.0438056 1.0031765]]
Q-values after update: [[1.0440168 1.0040636]]
Designated Priority: 1
Q-values before update: [[1.052264  1.0111133]]
Q-values after update: [[1.0511982 1.0114005]]
Designated Priority: 1
Q-values before update: [[1.0588024 1.0181075]]
Q-values after update: [[1.0566456 1.0178568]]
Designated Priority: 1
Q-values before update: [[1.0635028 1.0240928]]
Q-values after update: [[1.0604852 1.023379 ]]
Designated Priority: 1
Q-values before update: [[1.0665745 1.0291156]]
Q-values after update: [[1.0629729 1.0280383]]
Designated Priority: 1
Q-values before update: [[1.0682847 1.0332682]]
Q-values after update: [[1.0644331 1.0319679]]
Designated Priority: 1
Q-values before update: [[1.0574276 1.0277327]]
Q-values after update: [[1.0541052 1.0265642]]
Designated Priority: 1
Q-values before update: [[1.0333627 1.015291 ]]
Q-values after update: [[1.0325261 1.015465 ]]
Designated Priority: 3
Q-values before update: [[1.0096173 1.0027338]]
Q-values after update: [[1.0059456 1.001118 ]]
Episode 97 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.09452424 -1.7472708   0.23200102  2.798131  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0260426 1.0020113]]
Q-values after update: [[1.0235395 1.001313 ]]
Designated Priority: 1
Q-values before update: [[1.0310073 1.0078719]]
Q-values after update: [[1.0284393 1.0070807]]
Designated Priority: 1
Q-values before update: [[1.0351334 1.0131491]]
Q-values after update: [[1.0327111 1.0123587]]
Designated Priority: 1
Q-values before update: [[1.0387442 1.0180193]]
Q-values after update: [[1.0366893 1.0173343]]
Designated Priority: 1
Q-values before update: [[1.0419898 1.022501 ]]
Q-values after update: [[1.0405447 1.0220491]]
Designated Priority: 1
Q-values before update: [[1.0451326 1.0267498]]
Q-values after update: [[1.0445874 1.0267004]]
Designated Priority: 1
Q-values before update: [[1.0347172 1.0204597]]
Q-values after update: [[1.0361067 1.0214232]]
Designated Priority: 1
Q-values before update: [[1.0145261 1.009496 ]]
Q-values after update: [[1.0198593 1.0127286]]
Designated Priority: 3
Q-values before update: [[0.99645466 0.9995788 ]]
Q-values after update: [[1.0016508 1.0028788]]
Episode 98 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.14147961 -1.4002182   0.23764306  2.2239718 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.0273418 1.005681 ]]
Q-values after update: [[1.029808  1.0069776]]
Designated Priority: 1
Q-values before update: [[1.0221622 0.9998671]]
Q-values after update: [[1.0237968 1.0007138]]
Designated Priority: 1
Q-values before update: [[1.0322167 1.0083618]]
Q-values after update: [[1.0332725 1.009033 ]]
Designated Priority: 1
Q-values before update: [[1.0413063 1.0161364]]
Q-values after update: [[1.0418406 1.0166354]]
Designated Priority: 1
Q-values before update: [[1.049378 1.023488]]
Q-values after update: [[1.0494725 1.0238295]]
Designated Priority: 1
Q-values before update: [[1.0565   1.030365]]
Q-values after update: [[1.0562878 1.0305855]]
Designated Priority: 1
Q-values before update: [[1.0628047 1.0368077]]
Q-values after update: [[1.0624611 1.0369706]]
Designated Priority: 1
Q-values before update: [[1.0684439 1.042882 ]]
Q-values after update: [[1.0681833 1.043081 ]]
Designated Priority: 1
Q-values before update: [[1.0736376 1.0486891]]
Q-values after update: [[1.0736985 1.0490468]]
Designated Priority: 1
Q-values before update: [[1.0571007 1.0400352]]
Q-values after update: [[1.0592505 1.0415744]]
Designated Priority: 1
Q-values before update: [[1.0390397 1.0308529]]
Q-values after update: [[1.0449905 1.0346776]]
Designated Priority: 3
Q-values before update: [[1.0231119 1.0228716]]
Q-values after update: [[1.0206769 1.021503 ]]
Episode 99 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [-0.1369198  -1.9993306   0.23657356  3.036134  ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[1.0277591 1.0073931]]
Q-values after update: [[1.0261898 1.006822 ]]
Designated Priority: 1
Q-values before update: [[1.0350481 1.0146616]]
Q-values after update: [[1.0331826 1.0139339]]
Designated Priority: 1
Q-values before update: [[1.0413115 1.0212691]]
Q-values after update: [[1.0393012 1.0204471]]
Designated Priority: 1
Q-values before update: [[1.0467885 1.0274198]]
Q-values after update: [[1.0448133 1.0265812]]
Designated Priority: 1
Q-values before update: [[1.0515828 1.0330865]]
Q-values after update: [[1.0498569 1.0323328]]
Designated Priority: 1
Q-values before update: [[1.0559286 1.0383856]]
Q-values after update: [[1.0547055 1.0378535]]
Designated Priority: 1
Q-values before update: [[1.04668  1.032985]]
Q-values after update: [[1.0469431 1.0332274]]
Designated Priority: 1
Q-values before update: [[1.0270255 1.0226846]]
Q-values after update: [[1.0307782 1.0249461]]
Designated Priority: 3
Q-values before update: [[1.008991  1.0131366]]
Q-values after update: [[1.0100031 1.0113056]]
Episode 100 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.15098545 -1.4039724   0.25120303  2.2984421 ], Steps Taken: 9
"""

episode_pattern = r'Episode (\d+) out of total \d+, Total Reward: ([\d.]+), Epsilon: [\d.]+, Current State: \[.*\], Steps Taken: (\d+)'

matches = re.findall(episode_pattern, text)

episodes = []
rewards = []
steps = []

for match in matches:
    episodes.append(int(match[0]))
    rewards.append(float(match[1]))
    steps.append(int(match[2]))
    print(f"Episode: {match[0]}, Reward: {match[1]}, Steps Taken: {match[2]}")

rewards_all_runs = {i: [] for i in range(1, 6)}

for i, (episode, reward) in enumerate(zip(episodes, rewards)):
    repetition = (i % 5) + 1
    rewards_all_runs[repetition].append(reward)

print(f'Rewards per repetition: {rewards_all_runs}')

plt.figure(figsize=(10, 6))

for repetition in range(1, 6):
    if rewards_all_runs[repetition]:
        plt.plot(rewards_all_runs[repetition], label=f'Repetition {repetition}')
    else:
        print(f'No data for Repetition {repetition}')

max_length = min(len(run) for run in rewards_all_runs.values())
avg_rewards = np.mean([run[:max_length] for run in rewards_all_runs.values()], axis=0)

plt.plot(avg_rewards, label='Average Reward', color='black', linestyle='--', linewidth=2)

plt.xlabel('Episodes')
plt.ylabel('Total Reward')
plt.title('Total Reward per Episode Across 5 Repetitions')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
pip install python-docx

from docx import Document

doc = Document('/content/q-values for first ipynb.docx')

text = []

for para in doc.paragraphs:
    text.append(para.text)

for paragraph in text:
    print(paragraph)

import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve

text = """
Designated Priority: 1
Q-values before update: [[-0.01205321  0.01644367]]
Q-values after update: [[-0.01205298  0.03829568]]
Designated Priority: 1
Q-values before update: [[0.00028295 0.0349686 ]]
Q-values after update: [[-0.0001389   0.06784904]]
Designated Priority: 1
Q-values before update: [[0.00644842 0.08221429]]
Q-values after update: [[0.00621817 0.13602436]]
Designated Priority: 1
Q-values before update: [[0.01376624 0.17001885]]
Q-values after update: [[0.01110103 0.24656913]]
Designated Priority: 1
Q-values before update: [[0.01972094 0.30076557]]
Q-values after update: [[0.01395596 0.40216362]]
Designated Priority: 1
Q-values before update: [[0.02173006 0.4790102 ]]
Q-values after update: [[0.0120801  0.60888106]]
Designated Priority: 1
Q-values before update: [[0.01825202 0.7108943 ]]
Q-values after update: [[0.01579303 0.8639534 ]]
Designated Priority: 1
Q-values before update: [[0.01996264 0.99357814]]
Q-values after update: [[0.01826179 1.1598018 ]]
Designated Priority: 3
Q-values before update: [[0.02415863 1.3184915 ]]
Q-values after update: [[0.02457741 1.3676066 ]]
Episode 1 out of total 100, Total Reward: 9.0, Epsilon: 0.99, Current State: [ 0.18197596  1.7467027  -0.24977913 -2.819116  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[-0.02320418  0.15293375]]
Q-values after update: [[-0.02193851  0.16933459]]
Designated Priority: 1
Q-values before update: [[-0.00458095  0.30668178]]
Q-values after update: [[-0.00503734  0.32360193]]
Designated Priority: 1
Q-values before update: [[0.00047741 0.4746521 ]]
Q-values after update: [[0.00226078 0.5013624 ]]
Designated Priority: 1
Q-values before update: [[0.0059467 0.6556666]]
Q-values after update: [[0.00916775 0.6941482 ]]
Designated Priority: 1
Q-values before update: [[0.01434594 0.8589035 ]]
Q-values after update: [[0.01908997 0.9138654 ]]
Designated Priority: 1
Q-values before update: [[0.02589119 1.0919261 ]]
Q-values after update: [[0.03217147 1.1690207 ]]
Designated Priority: 1
Q-values before update: [[0.04070804 1.3637252 ]]
Q-values after update: [[0.0484909 1.4690695]]
Designated Priority: 1
Q-values before update: [[0.05886001 1.6841533 ]]
Q-values after update: [[0.06637923 1.818562  ]]
Designated Priority: 3
Q-values before update: [[0.07920849 2.0597143 ]]
Q-values after update: [[0.0738215 2.0299811]]
Episode 2 out of total 100, Total Reward: 9.0, Epsilon: 0.99, Current State: [ 0.14307961  1.7218336  -0.21467394 -2.7619624 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[-0.01779976  0.3112289 ]]
Q-values after update: [[-0.01601197  0.3216025 ]]
Designated Priority: 1
Q-values before update: [[-0.01188735  0.49934137]]
Q-values after update: [[-0.01283182  0.5035789 ]]
Designated Priority: 1
Q-values before update: [[0.00187936 0.70906985]]
Q-values after update: [[4.769750e-04 7.128377e-01]]
Designated Priority: 1
Q-values before update: [[0.01061282 0.9148675 ]]
Q-values after update: [[0.0086856 0.9211145]]
Designated Priority: 1
Q-values before update: [[0.01689463 1.124431  ]]
Q-values after update: [[0.01528049 1.1363943 ]]
Designated Priority: 1
Q-values before update: [[0.02363028 1.3445084 ]]
Q-values after update: [[0.02253017 1.3655328 ]]
Designated Priority: 1
Q-values before update: [[0.03114418 1.5806435 ]]
Q-values after update: [[0.03077149 1.6147126 ]]
Designated Priority: 1
Q-values before update: [[0.03977706 1.8392159 ]]
Q-values after update: [[0.04035199 1.8909943 ]]
Designated Priority: 1
Q-values before update: [[0.04988049 2.1274953 ]]
Q-values after update: [[0.05162473 2.2023723 ]]
Designated Priority: 3
Q-values before update: [[0.06181018 2.4536858 ]]
Q-values after update: [[0.0571577 2.3931143]]
Episode 3 out of total 100, Total Reward: 10.0, Epsilon: 0.99, Current State: [ 0.16983403  1.9592991  -0.26472628 -3.113627  ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[-0.01348621  0.43134916]]
Q-values after update: [[-0.01167785  0.43986797]]
Designated Priority: 1
Q-values before update: [[-0.012076    0.59056884]]
Q-values after update: [[-0.00719653  0.5942837 ]]
Designated Priority: 1
Q-values before update: [[-0.0042793  0.7889372]]
Q-values after update: [[0.00196258 0.7932904 ]]
Designated Priority: 1
Q-values before update: [[0.00983939 0.9848584 ]]
Q-values after update: [[0.01575097 0.9910845 ]]
Designated Priority: 1
Q-values before update: [[0.02189942 1.1823027 ]]
Q-values after update: [[0.03091449 1.1952406 ]]
Designated Priority: 1
Q-values before update: [[0.0389988 1.3917539]]
Q-values after update: [[0.05284946 1.4153519 ]]
Designated Priority: 1
Q-values before update: [[0.06207995 1.6185635 ]]
Q-values after update: [[0.08547998 1.6593947 ]]
Designated Priority: 1
Q-values before update: [[0.09873965 1.8735305 ]]
Q-values after update: [[0.13029489 1.934198  ]]
Designated Priority: 1
Q-values before update: [[0.14836283 2.1620884 ]]
Q-values after update: [[0.18866013 2.2472928 ]]
Designated Priority: 3
Q-values before update: [[0.21228692 2.4919105 ]]
Q-values after update: [[0.19107547 2.4109495 ]]
Episode 4 out of total 100, Total Reward: 10.0, Epsilon: 0.98, Current State: [ 0.19345863  1.921199   -0.21503638 -3.012331  ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.02427863 0.5906023 ]]
Q-values after update: [[0.02348759 0.5953131 ]]
Designated Priority: 1
Q-values before update: [[0.04242315 0.73862445]]
Q-values after update: [[0.04114039 0.7368008 ]]
Designated Priority: 1
Q-values before update: [[0.05524803 0.92327   ]]
Q-values after update: [[0.05223149 0.91522396]]
Designated Priority: 1
Q-values before update: [[0.06511569 1.1061811 ]]
Q-values after update: [[0.06165648 1.096303  ]]
Designated Priority: 1
Q-values before update: [[0.07396913 1.2889175 ]]
Q-values after update: [[0.07116415 1.2817025 ]]
Designated Priority: 1
Q-values before update: [[0.08314601 1.4755621 ]]
Q-values after update: [[0.08199416 1.4742154 ]]
Designated Priority: 1
Q-values before update: [[0.09379297 1.6710078 ]]
Q-values after update: [[0.09610304 1.680038  ]]
Designated Priority: 3
Q-values before update: [[0.10862232 1.8824183 ]]
Q-values after update: [[0.09620566 1.8388907 ]]
Episode 5 out of total 100, Total Reward: 8.0, Epsilon: 0.98, Current State: [ 0.13814321  1.5823889  -0.2108575  -2.5541558 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[0.01718843 0.6372978 ]]
Q-values after update: [[0.01669962 0.64927346]]
Designated Priority: 1
Q-values before update: [[0.03380713 0.7165189 ]]
Q-values after update: [[0.03209595 0.7216545 ]]
Designated Priority: 1
Q-values before update: [[0.03588306 0.8666992 ]]
Q-values after update: [[0.03241277 0.8747273 ]]
Designated Priority: 1
Q-values before update: [[0.0353583 1.0216064]]
Q-values after update: [[0.0311424 1.030664 ]]
Designated Priority: 1
Q-values before update: [[0.03603899 1.1863527 ]]
Q-values after update: [[0.03116795 1.2023702 ]]
Designated Priority: 1
Q-values before update: [[0.03551735 1.3624216 ]]
Q-values after update: [[0.03066804 1.3884482 ]]
Designated Priority: 1
Q-values before update: [[0.03623748 1.5561876 ]]
Q-values after update: [[0.02944965 1.5938746 ]]
Designated Priority: 1
Q-values before update: [[0.03573652 1.7707989 ]]
Q-values after update: [[0.02885525 1.8249881 ]]
Designated Priority: 1
Q-values before update: [[0.0343273 2.0119932]]
Q-values after update: [[0.02776437 2.086983  ]]
Designated Priority: 3
Q-values before update: [[0.03252241 2.2863183 ]]
Q-values after update: [[0.02752984 2.2216249 ]]
Episode 6 out of total 100, Total Reward: 10.0, Epsilon: 0.97, Current State: [ 0.15564694  1.9462763  -0.22992453 -3.0341885 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.02566497 0.8412545 ]]
Q-values after update: [[0.02703919 0.85439014]]
Designated Priority: 1
Q-values before update: [[0.0273588 0.8452068]]
Q-values after update: [[0.02864007 0.84874403]]
Designated Priority: 1
Q-values before update: [[0.01989358 0.9995671 ]]
Q-values after update: [[0.02000371 1.0011717 ]]
Designated Priority: 1
Q-values before update: [[0.0134995 1.1501837]]
Q-values after update: [[0.01408744 1.1547073 ]]
Designated Priority: 1
Q-values before update: [[0.01070689 1.3009353 ]]
Q-values after update: [[0.01217801 1.3113755 ]]
Designated Priority: 1
Q-values before update: [[0.00953437 1.4597294 ]]
Q-values after update: [[0.01226042 1.4796022 ]]
Designated Priority: 1
Q-values before update: [[0.00986978 1.6324409 ]]
Q-values after update: [[0.01445762 1.6658095 ]]
Designated Priority: 1
Q-values before update: [[0.0125462 1.8253602]]
Q-values after update: [[0.01971508 1.876984  ]]
Designated Priority: 3
Q-values before update: [[0.0179991 2.0467997]]
Q-values after update: [[0.01063046 1.9903525 ]]
Episode 7 out of total 100, Total Reward: 9.0, Epsilon: 0.97, Current State: [ 0.11369474  1.7278062  -0.25888816 -2.8667831 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[0.03281815 0.9892169 ]]
Q-values after update: [[0.03395829 1.004503  ]]
Designated Priority: 1
Q-values before update: [[0.03909563 0.91742617]]
Q-values after update: [[0.03947933 0.92191875]]
Designated Priority: 1
Q-values before update: [[0.03154724 1.0402013 ]]
Q-values after update: [[0.03099914 1.0399256 ]]
Designated Priority: 1
Q-values before update: [[0.02153106 1.1644679 ]]
Q-values after update: [[0.02126119 1.165616  ]]
Designated Priority: 1
Q-values before update: [[0.0157381 1.2884253]]
Q-values after update: [[0.01629433 1.2932903 ]]
Designated Priority: 1
Q-values before update: [[0.01176669 1.4164544 ]]
Q-values after update: [[0.01329517 1.4279592 ]]
Designated Priority: 1
Q-values before update: [[0.0087727 1.5534915]]
Q-values after update: [[0.01175697 1.5749934 ]]
Designated Priority: 1
Q-values before update: [[0.00739427 1.7045919 ]]
Q-values after update: [[0.01240274 1.7400637 ]]
Designated Priority: 1
Q-values before update: [[0.00839445 1.8756475 ]]
Q-values after update: [[0.01609027 1.9297595 ]]
Designated Priority: 3
Q-values before update: [[0.01267885 2.0735035 ]]
Q-values after update: [[0.00446559 2.0162199 ]]
Episode 8 out of total 100, Total Reward: 10.0, Epsilon: 0.96, Current State: [ 0.15748294  1.9268835  -0.2258271  -3.00344   ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.05212883 1.1749341 ]]
Q-values after update: [[0.05384484 1.1930951 ]]
Designated Priority: 1
Q-values before update: [[0.05556166 1.0489106 ]]
Q-values after update: [[0.05615804 1.0558467 ]]
Designated Priority: 1
Q-values before update: [[0.04049964 1.1350464 ]]
Q-values after update: [[0.0407467 1.1385133]]
Designated Priority: 1
Q-values before update: [[0.02718221 1.2426397 ]]
Q-values after update: [[0.02688403 1.2450051 ]]
Designated Priority: 1
Q-values before update: [[0.01852768 1.3499563 ]]
Q-values after update: [[0.01908735 1.3562084 ]]
Designated Priority: 1
Q-values before update: [[0.01185513 1.4605607 ]]
Q-values after update: [[0.01339269 1.4736142 ]]
Designated Priority: 1
Q-values before update: [[0.00605719 1.5796223 ]]
Q-values after update: [[0.00905092 1.6027768 ]]
Designated Priority: 1
Q-values before update: [[0.00175132 1.7120022 ]]
Q-values after update: [[0.00675654 1.7491523 ]]
Designated Priority: 1
Q-values before update: [[-3.2835454e-04  1.8633755e+00]]
Q-values after update: [[0.0073302 1.9190955]]
Designated Priority: 3
Q-values before update: [[6.861165e-04 2.040355e+00]]
Q-values after update: [[-0.00747492  1.9838732 ]]
Episode 9 out of total 100, Total Reward: 10.0, Epsilon: 0.96, Current State: [ 0.1535779   1.9835385  -0.24433604 -3.0499067 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.06753904 1.4051852 ]]
Q-values after update: [[0.06941693 1.4271313 ]]
Designated Priority: 1
Q-values before update: [[0.06327282 1.2017063 ]]
Q-values after update: [[0.06477013 1.2153888 ]]
Designated Priority: 1
Q-values before update: [[0.05256608 1.2528052 ]]
Q-values after update: [[0.05307136 1.2649194 ]]
Designated Priority: 1
Q-values before update: [[0.03894435 1.3131236 ]]
Q-values after update: [[0.04014371 1.3189687 ]]
Designated Priority: 1
Q-values before update: [[0.02835219 1.3989804 ]]
Q-values after update: [[0.03058989 1.4097891 ]]
Designated Priority: 1
Q-values before update: [[0.01885326 1.4899857 ]]
Q-values after update: [[0.022695  1.5088329]]
Designated Priority: 1
Q-values before update: [[0.01115438 1.5905979 ]]
Q-values after update: [[0.01725659 1.6211553 ]]
Designated Priority: 1
Q-values before update: [[0.00610041 1.7060983 ]]
Q-values after update: [[0.01520306 1.7526898 ]]
Designated Priority: 1
Q-values before update: [[0.00467462 1.8426908 ]]
Q-values after update: [[0.01760119 1.910387  ]]
Designated Priority: 3
Q-values before update: [[0.00800662 2.007644  ]]
Q-values after update: [[-1.4544651e-03  1.9496756e+00]]
Episode 10 out of total 100, Total Reward: 10.0, Epsilon: 0.95, Current State: [ 0.21757148  1.9449797  -0.21828742 -3.0095499 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.1004357 1.667485 ]]
Q-values after update: [[0.10256815 1.6925907 ]]
Designated Priority: 1
Q-values before update: [[0.09020883 1.4384955 ]]
Q-values after update: [[0.09182466 1.4561504 ]]
Designated Priority: 1
Q-values before update: [[0.06933738 1.4600629 ]]
Q-values after update: [[0.07038675 1.4791226 ]]
Designated Priority: 1
Q-values before update: [[0.05451632 1.4920142 ]]
Q-values after update: [[0.05611122 1.5189515 ]]
Designated Priority: 1
Q-values before update: [[0.03957826 1.5285181 ]]
Q-values after update: [[0.04228612 1.5671211 ]]
Designated Priority: 1
Q-values before update: [[0.02499896 1.585464  ]]
Q-values after update: [[0.03026085 1.6329199 ]]
Designated Priority: 1
Q-values before update: [[0.01221607 1.6659065 ]]
Q-values after update: [[0.02083197 1.7268116 ]]
Designated Priority: 1
Q-values before update: [[0.00293736 1.7713132 ]]
Q-values after update: [[0.01538511 1.8563992 ]]
Designated Priority: 3
Q-values before update: [[-1.5280768e-03  1.9101388e+00]]
Q-values after update: [[-0.01145655  1.8486559 ]]
Episode 11 out of total 100, Total Reward: 9.0, Epsilon: 0.95, Current State: [ 0.19144489  1.7755351  -0.24927767 -2.8911235 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[0.13341385 2.1234787 ]]
Q-values after update: [[0.13597605 2.156446  ]]
Designated Priority: 1
Q-values before update: [[0.11879826 1.7711844 ]]
Q-values after update: [[0.15525775 1.7895466 ]]
Designated Priority: 1
Q-values before update: [[0.18517107 2.220746  ]]
Q-values after update: [[0.22845513 2.265809  ]]
Designated Priority: 1
Q-values before update: [[0.19261882 1.8396223 ]]
Q-values after update: [[0.22658472 1.8842198 ]]
Designated Priority: 1
Q-values before update: [[0.19035868 1.7116814 ]]
Q-values after update: [[0.21704794 1.7392936 ]]
Designated Priority: 1
Q-values before update: [[0.18468438 1.712638  ]]
Q-values after update: [[0.20844549 1.7389497 ]]
Designated Priority: 1
Q-values before update: [[0.18813841 1.7312351 ]]
Q-values after update: [[0.21179818 1.7657158 ]]
Designated Priority: 1
Q-values before update: [[0.19143854 1.7589335 ]]
Q-values after update: [[0.21613787 1.8053747 ]]
Designated Priority: 1
Q-values before update: [[0.19597764 1.8011972 ]]
Q-values after update: [[0.22313583 1.8642955 ]]
Designated Priority: 1
Q-values before update: [[0.20355578 1.864785  ]]
Q-values after update: [[0.23488879 1.9503139 ]]
Designated Priority: 1
Q-values before update: [[0.21642077 1.9580194 ]]
Q-values after update: [[0.2539639 2.0729373]]
Designated Priority: 1
Q-values before update: [[0.23731583 2.0909731 ]]
Q-values after update: [[0.28344363 2.2435145 ]]
Designated Priority: 3
Q-values before update: [[0.26952395 2.2756312 ]]
Q-values after update: [[0.2521695 2.1468139]]
Episode 12 out of total 100, Total Reward: 13.0, Epsilon: 0.94, Current State: [ 0.2349397   2.101839   -0.25533321 -3.2375062 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[0.53591025 2.7369406 ]]
Q-values after update: [[0.5549895 2.7640355]]
Designated Priority: 1
Q-values before update: [[0.47013572 2.2707615 ]]
Q-values after update: [[0.48586255 2.3005896 ]]
Designated Priority: 1
Q-values before update: [[0.40839183 2.0401635 ]]
Q-values after update: [[0.42007884 2.0522275 ]]
Designated Priority: 1
Q-values before update: [[0.3582601 1.9523532]]
Q-values after update: [[0.36422148 1.9513359 ]]
Designated Priority: 1
Q-values before update: [[0.33695042 1.918898  ]]
Q-values after update: [[0.34306696 1.9215537 ]]
Designated Priority: 1
Q-values before update: [[0.3144562 1.8837982]]
Q-values after update: [[0.3216718 1.893554 ]]
Designated Priority: 1
Q-values before update: [[0.2918989 1.8517196]]
Q-values after update: [[0.30137184 1.8728151 ]]
Designated Priority: 1
Q-values before update: [[0.2707103 1.8284569]]
Q-values after update: [[0.28383845 1.8660649 ]]
Designated Priority: 1
Q-values before update: [[0.25296083 1.8226866 ]]
Q-values after update: [[0.27127075 1.8822167 ]]
Designated Priority: 3
Q-values before update: [[0.24481212 1.8467273 ]]
Q-values after update: [[0.2325889 1.7690357]]
Episode 13 out of total 100, Total Reward: 10.0, Epsilon: 0.94, Current State: [ 0.12433465  1.9098973  -0.24000046 -3.0383098 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[0.7011552 3.0758   ]]
Q-values after update: [[0.71418417 3.1119175 ]]
Designated Priority: 1
Q-values before update: [[0.6042602 2.5494804]]
Q-values after update: [[0.6183466 2.5962684]]
Designated Priority: 1
Q-values before update: [[0.5240325 2.2886455]]
Q-values after update: [[0.5400814 2.3246953]]
Designated Priority: 1
Q-values before update: [[0.45492423 2.128294  ]]
Q-values after update: [[0.46930876 2.1615872 ]]
Designated Priority: 1
Q-values before update: [[0.4064022 2.0137193]]
Q-values after update: [[0.42004073 2.0481973 ]]
Designated Priority: 1
Q-values before update: [[0.36520743 1.9191797 ]]
Q-values after update: [[0.37709874 1.9521018 ]]
Designated Priority: 1
Q-values before update: [[0.3328511 1.8509103]]
Q-values after update: [[0.34599423 1.8920215 ]]
Designated Priority: 3
Q-values before update: [[0.3038571 1.7960199]]
Q-values after update: [[0.28897813 1.7259092 ]]
Episode 14 out of total 100, Total Reward: 8.0, Epsilon: 0.93, Current State: [ 0.15757614  1.590386   -0.218135   -2.5768564 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[0.8444499 3.5999064]]
Q-values after update: [[0.8570762 3.647229 ]]
Designated Priority: 1
Q-values before update: [[0.7477615 3.0869806]]
Q-values after update: [[0.761701  3.1430368]]
Designated Priority: 1
Q-values before update: [[0.654645 2.656682]]
Q-values after update: [[0.6702849 2.7061384]]
Designated Priority: 1
Q-values before update: [[0.58481556 2.447826  ]]
Q-values after update: [[0.60475814 2.503393  ]]
Designated Priority: 1
Q-values before update: [[0.5130473 2.2594018]]
Q-values after update: [[0.53204775 2.3142676 ]]
Designated Priority: 1
Q-values before update: [[0.45594648 2.107893  ]]
Q-values after update: [[0.4810617 2.1817784]]
Designated Priority: 1
Q-values before update: [[0.40482324 1.9728242 ]]
Q-values after update: [[0.4376384 2.0715077]]
Designated Priority: 1
Q-values before update: [[0.36174902 1.8620125 ]]
Q-values after update: [[0.40413016 1.9924432 ]]
Designated Priority: 1
Q-values before update: [[0.329266  1.7851003]]
Q-values after update: [[0.38371265 1.9568586 ]]
Designated Priority: 3
Q-values before update: [[0.32124296 1.78891   ]]
Q-values after update: [[0.295762  1.6899049]]
Episode 15 out of total 100, Total Reward: 10.0, Epsilon: 0.93, Current State: [ 0.21389931  1.9686334  -0.25788566 -3.105594  ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[1.0078026 4.2667627]]
Q-values after update: [[1.0183069 4.315778 ]]
Designated Priority: 1
Q-values before update: [[0.9139651 3.7474744]]
Q-values after update: [[0.92461985 3.8039403 ]]
Designated Priority: 1
Q-values before update: [[0.81513476 3.2159076 ]]
Q-values after update: [[0.8255745 3.2583747]]
Designated Priority: 1
Q-values before update: [[0.74061066 2.9301133 ]]
Q-values after update: [[0.75334907 2.9781902 ]]
Designated Priority: 1
Q-values before update: [[0.65337795 2.6842115 ]]
Q-values after update: [[0.6691479 2.7377653]]
Designated Priority: 1
Q-values before update: [[0.56934375 2.444493  ]]
Q-values after update: [[0.5911621 2.516865 ]]
Designated Priority: 1
Q-values before update: [[0.49039346 2.2178295 ]]
Q-values after update: [[0.5201345 2.3157759]]
Designated Priority: 3
Q-values before update: [[0.41898292 2.0132723 ]]
Q-values after update: [[0.3717704 1.8417788]]
Episode 16 out of total 100, Total Reward: 8.0, Epsilon: 0.92, Current State: [ 0.16049886  1.6088084  -0.21316049 -2.550637  ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[1.1091446 4.7843075]]
Q-values after update: [[1.1124642 4.8081303]]
Designated Priority: 1
Q-values before update: [[0.998083  4.2076907]]
Q-values after update: [[0.9984572 4.2278914]]
Designated Priority: 1
Q-values before update: [[0.8682146 3.4925451]]
Q-values after update: [[0.86817914 3.5186594 ]]
Designated Priority: 1
Q-values before update: [[0.74916583 3.0117364 ]]
Q-values after update: [[0.7443682 3.0049684]]
Designated Priority: 1
Q-values before update: [[0.6108422 2.5573072]]
Q-values after update: [[0.607937 2.558303]]
Designated Priority: 1
Q-values before update: [[0.47287244 2.1102192 ]]
Q-values after update: [[0.4694929 2.103946 ]]
Designated Priority: 1
Q-values before update: [[0.33776358 1.6806995 ]]
Q-values after update: [[0.33685827 1.6795671 ]]
Designated Priority: 1
Q-values before update: [[0.20820677 1.2756809 ]]
Q-values after update: [[0.21328919 1.2989911 ]]
Designated Priority: 3
Q-values before update: [[0.17003314 1.109072  ]]
Q-values after update: [[0.16961335 1.1107919 ]]
Episode 17 out of total 100, Total Reward: 9.0, Epsilon: 0.92, Current State: [ 0.17548051  1.7565926  -0.2574442  -2.9081576 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.1946989 5.3003917]]
Q-values after update: [[1.20913  5.377759]]
Designated Priority: 1
Q-values before update: [[1.0816121 4.7583776]]
Q-values after update: [[1.0955727 4.839453 ]]
Designated Priority: 1
Q-values before update: [[0.95555854 4.094539  ]]
Q-values after update: [[0.9709176 4.188229 ]]
Designated Priority: 1
Q-values before update: [[0.8306181 3.4723525]]
Q-values after update: [[0.8477622 3.5823827]]
Designated Priority: 1
Q-values before update: [[0.70065916 3.00007   ]]
Q-values after update: [[0.7199194 3.0948281]]
Designated Priority: 1
Q-values before update: [[0.57900006 2.603761  ]]
Q-values after update: [[0.60384965 2.7228756 ]]
Designated Priority: 1
Q-values before update: [[0.4617357 2.2292476]]
Q-values after update: [[0.49394178 2.3795662 ]]
Designated Priority: 1
Q-values before update: [[0.35345858 1.8984269 ]]
Q-values after update: [[0.3958647 2.090011 ]]
Designated Priority: 3
Q-values before update: [[0.2766198 1.6881115]]
Q-values after update: [[0.24471252 1.5573796 ]]
Episode 18 out of total 100, Total Reward: 9.0, Epsilon: 0.91, Current State: [ 0.17373455  1.7368398  -0.22436546 -2.836947  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[1.3675977 6.215101 ]]
Q-values after update: [[1.3769727 6.270664 ]]
Designated Priority: 1
Q-values before update: [[1.2530879 5.703066 ]]
Q-values after update: [[1.2627212 5.7632604]]
Designated Priority: 1
Q-values before update: [[1.1211714 5.082738 ]]
Q-values after update: [[1.1317679 5.1474514]]
Designated Priority: 1
Q-values before update: [[0.99181557 4.417983  ]]
Q-values after update: [[1.0012196 4.48161  ]]
Designated Priority: 1
Q-values before update: [[0.84449536 3.8036528 ]]
Q-values after update: [[0.85628617 3.8823798 ]]
Designated Priority: 1
Q-values before update: [[0.6953567 3.1877477]]
Q-values after update: [[0.7883306 3.3104515]]
Designated Priority: 1
Q-values before update: [[0.9536448 3.9753587]]
Q-values after update: [[1.0488662 4.1048813]]
Designated Priority: 1
Q-values before update: [[0.8691232 3.3846872]]
Q-values after update: [[0.96001285 3.5353694 ]]
Designated Priority: 1
Q-values before update: [[0.7731274 2.806687 ]]
Q-values after update: [[0.8644748 2.9897258]]
Designated Priority: 1
Q-values before update: [[0.67086333 2.2531226 ]]
Q-values after update: [[0.76782   2.4797873]]
Designated Priority: 3
Q-values before update: [[0.5702541 1.7508413]]
Q-values after update: [[0.54163307 1.5685669 ]]
Episode 19 out of total 100, Total Reward: 11.0, Epsilon: 0.91, Current State: [ 0.20846729  1.7729263  -0.22325598 -2.7526412 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[1.9861549 7.0297003]]
Q-values after update: [[2.0431244 7.0588775]]
Designated Priority: 1
Q-values before update: [[1.8759798 6.462592 ]]
Q-values after update: [[1.9228474 6.48915  ]]
Designated Priority: 1
Q-values before update: [[1.7314122 5.7465997]]
Q-values after update: [[1.7690251 5.764342 ]]
Designated Priority: 1
Q-values before update: [[1.556598 4.936322]]
Q-values after update: [[1.5849739 4.9500036]]
Designated Priority: 1
Q-values before update: [[1.3370702 4.0921397]]
Q-values after update: [[1.3564848 4.0933113]]
Designated Priority: 1
Q-values before update: [[1.1179621 3.2950313]]
Q-values after update: [[1.2086879 3.3561795]]
Designated Priority: 1
Q-values before update: [[1.4145038 4.0322165]]
Q-values after update: [[1.5091548 4.11576  ]]
Designated Priority: 1
Q-values before update: [[1.2370212 3.2417667]]
Q-values after update: [[1.3874975 3.3774939]]
Designated Priority: 1
Q-values before update: [[1.5921049 4.0366597]]
Q-values after update: [[1.7400482 4.1760144]]
Designated Priority: 3
Q-values before update: [[1.436101 3.239875]]
Q-values after update: [[1.3588959 2.7956133]]
Episode 20 out of total 100, Total Reward: 10.0, Epsilon: 0.90, Current State: [ 0.12023181  1.2249143  -0.22314626 -1.9873748 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[2.8850226 7.4920607]]
Q-values after update: [[2.9422512 7.353211 ]]
Designated Priority: 1
Q-values before update: [[2.699527 6.677288]]
Q-values after update: [[2.734174 6.526671]]
Designated Priority: 1
Q-values before update: [[2.4593568 5.6701975]]
Q-values after update: [[2.4706364 5.5027795]]
Designated Priority: 1
Q-values before update: [[2.1506028 4.552015 ]]
Q-values after update: [[2.136619  4.3683434]]
Designated Priority: 1
Q-values before update: [[1.7651616 3.3420784]]
Q-values after update: [[1.7323592 3.1472101]]
Designated Priority: 1
Q-values before update: [[1.3121657 2.086561 ]]
Q-values after update: [[1.2564113 1.9054742]]
Designated Priority: 1
Q-values before update: [[0.78325194 0.9905736 ]]
Q-values after update: [[0.73905754 0.89793414]]
Designated Priority: 1
Q-values before update: [[0.5541049  0.59998894]]
Q-values after update: [[0.5523117 0.570015 ]]
Designated Priority: 1
Q-values before update: [[0.526273   0.46795365]]
Q-values after update: [[0.5373486  0.45215344]]
Designated Priority: 3
Q-values before update: [[0.5550615  0.51733404]]
Q-values after update: [[0.5842221 0.5118067]]
Episode 21 out of total 100, Total Reward: 10.0, Epsilon: 0.90, Current State: [ 0.1912877   1.1574906  -0.24142706 -1.940009  ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[3.1584995 6.419503 ]]
Q-values after update: [[3.1875217 6.3841553]]
Designated Priority: 1
Q-values before update: [[2.8124151 5.4630365]]
Q-values after update: [[2.8301027 5.4169574]]
Designated Priority: 1
Q-values before update: [[2.4206727 4.334555 ]]
Q-values after update: [[2.4273102 4.278002 ]]
Designated Priority: 1
Q-values before update: [[1.9650493 3.1207962]]
Q-values after update: [[1.9617928 3.0540287]]
Designated Priority: 1
Q-values before update: [[1.4477211 1.9021878]]
Q-values after update: [[1.4351922 1.8452106]]
Designated Priority: 1
Q-values before update: [[0.9157759 0.9334153]]
Q-values after update: [[0.9406248 0.9363122]]
Designated Priority: 1
Q-values before update: [[1.3612103 1.666958 ]]
Q-values after update: [[1.3818607 1.6628455]]
Designated Priority: 1
Q-values before update: [[0.8831306  0.82726514]]
Q-values after update: [[0.9296453 0.855434 ]]
Designated Priority: 1
Q-values before update: [[1.2866583 1.4516159]]
Q-values after update: [[1.3310556 1.4837096]]
Designated Priority: 3
Q-values before update: [[0.92625946 0.80950934]]
Q-values after update: [[0.9770934  0.84681547]]
Episode 22 out of total 100, Total Reward: 10.0, Epsilon: 0.90, Current State: [ 0.09172805  0.83695865 -0.21509568 -1.4413351 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[3.4622939 6.321813 ]]
Q-values after update: [[3.4936476 6.326043 ]]
Designated Priority: 1
Q-values before update: [[3.096506  5.4091845]]
Q-values after update: [[3.1239812 5.4132147]]
Designated Priority: 1
Q-values before update: [[2.7057867 4.3544707]]
Q-values after update: [[2.7301235 4.3585234]]
Designated Priority: 1
Q-values before update: [[2.281798  3.2549946]]
Q-values after update: [[2.3048387 3.2613611]]
Designated Priority: 1
Q-values before update: [[1.8158488 2.1881504]]
Q-values after update: [[1.8405323 2.2034626]]
Designated Priority: 1
Q-values before update: [[1.3249806 1.2556186]]
Q-values after update: [[1.3826082 1.3065906]]
Designated Priority: 1
Q-values before update: [[1.8225257 2.1159594]]
Q-values after update: [[1.8720603 2.1645012]]
Designated Priority: 1
Q-values before update: [[1.3709923 1.2494648]]
Q-values after update: [[1.4455421 1.3197803]]
Designated Priority: 1
Q-values before update: [[1.8293622 2.0192778]]
Q-values after update: [[1.9021178 2.0973175]]
Designated Priority: 1
Q-values before update: [[1.4855541 1.3150537]]
Q-values after update: [[1.577924  1.4058665]]
Designated Priority: 3
Q-values before update: [[1.9081873 2.0101898]]
Q-values after update: [[1.8899809 1.9253008]]
Episode 23 out of total 100, Total Reward: 11.0, Epsilon: 0.89, Current State: [ 0.14399001  0.9481658  -0.22812721 -1.750345  ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[3.8395598 6.422892 ]]
Q-values after update: [[3.8525105 6.381987 ]]
Designated Priority: 1
Q-values before update: [[3.4625547 5.510747 ]]
Q-values after update: [[3.4693708 5.4659095]]
Designated Priority: 1
Q-values before update: [[3.063871  4.4600434]]
Q-values after update: [[3.0657184 4.413024 ]]
Designated Priority: 1
Q-values before update: [[2.639582  3.3663054]]
Q-values after update: [[2.6372528 3.3183093]]
Designated Priority: 1
Q-values before update: [[2.1609023 2.283776 ]]
Q-values after update: [[2.1611352 2.2491872]]
Designated Priority: 1
Q-values before update: [[1.7090353 1.3952762]]
Q-values after update: [[1.736532  1.3978075]]
Designated Priority: 1
Q-values before update: [[2.1070333 2.095968 ]]
Q-values after update: [[2.1577358 2.1124578]]
Designated Priority: 1
Q-values before update: [[2.5488358 2.9780805]]
Q-values after update: [[2.594006  2.9901934]]
Designated Priority: 1
Q-values before update: [[2.0904288 1.9236041]]
Q-values after update: [[2.1633663 1.9656467]]
Designated Priority: 1
Q-values before update: [[2.5329733 2.775863 ]]
Q-values after update: [[2.5997534 2.8151696]]
Designated Priority: 1
Q-values before update: [[2.0935512 1.7967937]]
Q-values after update: [[2.1819015 1.8568572]]
Designated Priority: 3
Q-values before update: [[2.524842  2.5614197]]
Q-values after update: [[2.4927661 2.4179716]]
Episode 24 out of total 100, Total Reward: 12.0, Epsilon: 0.89, Current State: [ 0.16417637  0.74407643 -0.22845206 -1.4984989 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.197878 6.157993]]
Q-values after update: [[4.2113843 6.081507 ]]
Designated Priority: 1
Q-values before update: [[3.7977378 5.191621 ]]
Q-values after update: [[3.802897 5.112643]]
Designated Priority: 1
Q-values before update: [[3.3799748 4.106841 ]]
Q-values after update: [[3.4311597 4.0542865]]
Designated Priority: 1
Q-values before update: [[3.8579724 5.0572047]]
Q-values after update: [[3.9120798 5.011406 ]]
Designated Priority: 1
Q-values before update: [[3.4606984 3.9815686]]
Q-values after update: [[3.5000246 3.9362638]]
Designated Priority: 1
Q-values before update: [[3.0002136 2.8699965]]
Q-values after update: [[3.0552695 2.847119 ]]
Designated Priority: 1
Q-values before update: [[3.5173287 3.8303423]]
Q-values after update: [[3.577329  3.8118787]]
Designated Priority: 1
Q-values before update: [[3.0375402 2.7165003]]
Q-values after update: [[3.110961  2.7189763]]
Designated Priority: 1
Q-values before update: [[3.5751226 3.6663518]]
Q-values after update: [[3.65112   3.6718872]]
Designated Priority: 1
Q-values before update: [[3.073759 2.553689]]
Q-values after update: [[3.1629539 2.5793107]]
Designated Priority: 1
Q-values before update: [[3.6260033 3.4880047]]
Q-values after update: [[3.7442563 3.5250099]]
Designated Priority: 1
Q-values before update: [[4.154094 4.394916]]
Q-values after update: [[4.2669244 4.4268436]]
Designated Priority: 1
Q-values before update: [[3.7047536 3.3117168]]
Q-values after update: [[3.8112328 3.3609226]]
Designated Priority: 1
Q-values before update: [[3.1730456 2.2947083]]
Q-values after update: [[3.2953825 2.3635192]]
Designated Priority: 1
Q-values before update: [[3.7347844 3.1145768]]
Q-values after update: [[3.8751197 3.188913 ]]
Designated Priority: 1
Q-values before update: [[4.269483  3.9743261]]
Q-values after update: [[4.433474  4.0522513]]
Designated Priority: 1
Q-values before update: [[4.786473  4.7721896]]
Q-values after update: [[4.982764 4.855136]]
Designated Priority: 1
Q-values before update: [[5.3407903 5.522945 ]]
Q-values after update: [[5.5301642 5.603401 ]]
Designated Priority: 3
Q-values before update: [[4.9511123 4.6000924]]
Q-values after update: [[4.7637773 4.488558 ]]
Episode 25 out of total 100, Total Reward: 19.0, Epsilon: 0.88, Current State: [ 0.1117183  -0.18264015 -0.210349   -0.27494264], Steps Taken: 19
Designated Priority: 1
Q-values before update: [[5.984515 6.297041]]
Q-values after update: [[5.8347425 6.233395 ]]
Designated Priority: 1
Q-values before update: [[5.3354673 5.3580704]]
Q-values after update: [[5.212049  5.3086224]]
Designated Priority: 1
Q-values before update: [[4.705937 4.313876]]
Q-values after update: [[4.62017   4.2747016]]
Designated Priority: 1
Q-values before update: [[5.0885015 5.227734 ]]
Q-values after update: [[5.0368733 5.2130246]]
Designated Priority: 1
Q-values before update: [[5.5030665 6.0709767]]
Q-values after update: [[5.4537907 6.059274 ]]
Designated Priority: 1
Q-values before update: [[4.959048 5.149783]]
Q-values after update: [[4.920488 5.144461]]
Designated Priority: 1
Q-values before update: [[4.4093084 4.1074386]]
Q-values after update: [[4.395083  4.1088147]]
Designated Priority: 1
Q-values before update: [[4.84055   5.0523252]]
Q-values after update: [[4.829715  5.0631456]]
Designated Priority: 1
Q-values before update: [[4.3118896 4.0034986]]
Q-values after update: [[4.321876  4.0204463]]
Designated Priority: 1
Q-values before update: [[4.7499356 4.9461684]]
Q-values after update: [[4.7867007 4.9814425]]
Designated Priority: 1
Q-values before update: [[5.210165 5.81652 ]]
Q-values after update: [[5.240306 5.843938]]
Designated Priority: 1
Q-values before update: [[4.73074   4.8686347]]
Q-values after update: [[4.7638087 4.9038367]]
Designated Priority: 1
Q-values before update: [[4.2264276 3.8060198]]
Q-values after update: [[4.271401 3.844011]]
Designated Priority: 1
Q-values before update: [[4.678625  4.7419825]]
Q-values after update: [[4.7255664 4.7887964]]
Designated Priority: 1
Q-values before update: [[4.1758223 3.6687024]]
Q-values after update: [[4.233072 3.717497]]
Designated Priority: 1
Q-values before update: [[4.62003  4.587422]]
Q-values after update: [[4.6996026 4.6527348]]
Designated Priority: 1
Q-values before update: [[5.069743 5.453958]]
Q-values after update: [[5.137483 5.507055]]
Designated Priority: 1
Q-values before update: [[4.602245  4.4436746]]
Q-values after update: [[4.6929307 4.51537  ]]
Designated Priority: 1
Q-values before update: [[5.043612 5.302907]]
Q-values after update: [[5.1229463 5.3648763]]
Designated Priority: 1
Q-values before update: [[4.585699 4.284888]]
Q-values after update: [[4.684897  4.3630457]]
Designated Priority: 1
Q-values before update: [[5.0075545 5.115568 ]]
Q-values after update: [[5.0968556 5.1881366]]
Designated Priority: 1
Q-values before update: [[4.5644236 4.1095886]]
Q-values after update: [[4.6729665 4.1981115]]
Designated Priority: 1
Q-values before update: [[4.9660087 4.9156613]]
Q-values after update: [[5.0839496 5.0042005]]
Designated Priority: 1
Q-values before update: [[5.3618712 5.6454716]]
Q-values after update: [[5.465844  5.7224207]]
Designated Priority: 1
Q-values before update: [[4.961574  4.7334948]]
Q-values after update: [[5.0869474 4.828446 ]]
Designated Priority: 1
Q-values before update: [[5.342333 5.458592]]
Q-values after update: [[5.4559774 5.547725 ]]
Designated Priority: 3
Q-values before update: [[4.984758  4.5720634]]
Q-values after update: [[4.8041306 4.463937 ]]
Episode 26 out of total 100, Total Reward: 27.0, Epsilon: 0.88, Current State: [ 0.06916343 -0.1299222  -0.2198879  -0.4803743 ], Steps Taken: 27
Designated Priority: 1
Q-values before update: [[6.6434646 7.1139703]]
Q-values after update: [[6.519069 7.07109 ]]
Designated Priority: 1
Q-values before update: [[6.118986 6.283911]]
Q-values after update: [[6.0036297 6.2423754]]
Designated Priority: 1
Q-values before update: [[5.5487313 5.2616525]]
Q-values after update: [[5.464897  5.2289443]]
Designated Priority: 1
Q-values before update: [[5.863481 6.139557]]
Q-values after update: [[5.792876  6.1214733]]
Designated Priority: 1
Q-values before update: [[5.319845 5.106545]]
Q-values after update: [[5.278319  5.0992126]]
Designated Priority: 1
Q-values before update: [[5.668505 6.002151]]
Q-values after update: [[5.6326656 6.0016365]]
Designated Priority: 1
Q-values before update: [[5.145032 4.958412]]
Q-values after update: [[5.136077  4.9702663]]
Designated Priority: 1
Q-values before update: [[5.5124145 5.857437 ]]
Q-values after update: [[5.530937 5.884356]]
Designated Priority: 1
Q-values before update: [[5.892712  6.6524534]]
Q-values after update: [[5.9086056 6.6762714]]
Designated Priority: 1
Q-values before update: [[5.4434423 5.752137 ]]
Q-values after update: [[5.458983 5.776777]]
Designated Priority: 1
Q-values before update: [[4.950549  4.6978855]]
Q-values after update: [[4.987802 4.736426]]
Designated Priority: 1
Q-values before update: [[5.3353105 5.5862446]]
Q-values after update: [[5.367424  5.6218047]]
Designated Priority: 1
Q-values before update: [[4.8463206 4.5218015]]
Q-values after update: [[4.8991904 4.5721397]]
Designated Priority: 1
Q-values before update: [[5.220534  5.3875375]]
Q-values after update: [[5.265903 5.433561]]
Designated Priority: 1
Q-values before update: [[4.733571  4.3134956]]
Q-values after update: [[4.7988243 4.374772 ]]
Designated Priority: 1
Q-values before update: [[5.087803  5.1484876]]
Q-values after update: [[5.1645823 5.213808 ]]
Designated Priority: 1
Q-values before update: [[5.439772  5.9249177]]
Q-values after update: [[5.502436  5.9752417]]
Designated Priority: 1
Q-values before update: [[4.987137  4.9105515]]
Q-values after update: [[5.0714364 4.978822 ]]
Designated Priority: 1
Q-values before update: [[5.315768  5.6577725]]
Q-values after update: [[5.3861694 5.7136383]]
Designated Priority: 1
Q-values before update: [[4.8656993 4.6329603]]
Q-values after update: [[4.9559035 4.7062454]]
Designated Priority: 1
Q-values before update: [[5.1644993 5.3465323]]
Q-values after update: [[5.2413354 5.4101286]]
Designated Priority: 1
Q-values before update: [[4.7149673 4.311999 ]]
Q-values after update: [[4.8101807 4.392235 ]]
Designated Priority: 3
Q-values before update: [[4.977657  4.9886103]]
Q-values after update: [[4.876194 4.742521]]
Episode 27 out of total 100, Total Reward: 23.0, Epsilon: 0.87, Current State: [ 0.09980291  0.2601915  -0.22104734 -0.9435532 ], Steps Taken: 23
Designated Priority: 1
Q-values before update: [[6.726873 7.20305 ]]
Q-values after update: [[6.6767535 7.005627 ]]
Designated Priority: 1
Q-values before update: [[6.266889  6.1715174]]
Q-values after update: [[6.233097  6.0001545]]
Designated Priority: 1
Q-values before update: [[6.5547137 6.7180753]]
Q-values after update: [[6.5564775 6.5828924]]
Designated Priority: 1
Q-values before update: [[6.8899536 7.218307 ]]
Q-values after update: [[6.949416 7.112614]]
Designated Priority: 1
Q-values before update: [[7.4172564 7.745615 ]]
Q-values after update: [[7.501703  7.6772223]]
Designated Priority: 1
Q-values before update: [[6.9625626 6.9807324]]
Q-values after update: [[7.014411 6.914149]]
Designated Priority: 1
Q-values before update: [[6.5373535 6.173325 ]]
Q-values after update: [[6.5652146 6.117099 ]]
Designated Priority: 1
Q-values before update: [[6.075501  5.2114096]]
Q-values after update: [[6.105018 5.166774]]
Designated Priority: 1
Q-values before update: [[6.4951787 5.949941 ]]
Q-values after update: [[6.5496345 5.9204273]]
Designated Priority: 1
Q-values before update: [[6.997539 6.606176]]
Q-values after update: [[7.073107  6.6068664]]
Designated Priority: 1
Q-values before update: [[6.514312  5.8012304]]
Q-values after update: [[6.580981 5.796052]]
Designated Priority: 1
Q-values before update: [[7.0535593 6.5082126]]
Q-values after update: [[7.172833  6.5324416]]
Designated Priority: 1
Q-values before update: [[7.8026457 7.2903185]]
Q-values after update: [[7.95792   7.3639517]]
Designated Priority: 1
Q-values before update: [[7.21921   6.5026464]]
Q-values after update: [[7.3680625 6.558675 ]]
Designated Priority: 1
Q-values before update: [[8.074442 7.384162]]
Q-values after update: [[8.307703 7.489186]]
Designated Priority: 1
Q-values before update: [[9.177063 8.364975]]
Q-values after update: [[9.531598 8.531768]]
Designated Priority: 1
Q-values before update: [[10.524379  9.482991]]
Q-values after update: [[11.030504  9.721423]]
Designated Priority: 1
Q-values before update: [[12.15515  10.759035]]
Q-values after update: [[12.872029 11.102139]]
Designated Priority: 1
Q-values before update: [[14.157508 12.241239]]
Q-values after update: [[15.143021 12.720891]]
Designated Priority: 1
Q-values before update: [[16.623558 13.979725]]
Q-values after update: [[17.960604 14.638327]]
Designated Priority: 1
Q-values before update: [[19.678764 16.04087 ]]
Q-values after update: [[21.474976 16.935347]]
Designated Priority: 1
Q-values before update: [[23.484987 18.512932]]
Q-values after update: [[25.870592 19.72139 ]]
Designated Priority: 3
Q-values before update: [[28.235704 21.509975]]
Q-values after update: [[26.092096 20.213253]]
Episode 28 out of total 100, Total Reward: 23.0, Epsilon: 0.87, Current State: [-0.18685825 -2.0947948   0.22701466  3.0690265 ], Steps Taken: 23
Designated Priority: 1
Q-values before update: [[9.731682  7.3987355]]
Q-values after update: [[9.320732 7.181   ]]
Designated Priority: 1
Q-values before update: [[10.60436   8.313814]]
Q-values after update: [[10.127479  8.049337]]
Designated Priority: 1
Q-values before update: [[11.443535  9.132124]]
Q-values after update: [[10.926684  8.831874]]
Designated Priority: 1
Q-values before update: [[12.2234955  9.875625 ]]
Q-values after update: [[11.684539  9.54906 ]]
Designated Priority: 1
Q-values before update: [[12.944739 10.57425 ]]
Q-values after update: [[12.398039 10.232233]]
Designated Priority: 1
Q-values before update: [[13.621521 11.236932]]
Q-values after update: [[13.072917 10.945849]]
Designated Priority: 1
Q-values before update: [[12.080811 10.126876]]
Q-values after update: [[11.659687  9.904132]]
Designated Priority: 1
Q-values before update: [[12.820659 10.880123]]
Q-values after update: [[12.400228 10.64795 ]]
Designated Priority: 1
Q-values before update: [[13.550184 11.62558 ]]
Q-values after update: [[13.144182 11.392761]]
Designated Priority: 1
Q-values before update: [[14.307019 12.385366]]
Q-values after update: [[13.916816 12.154699]]
Designated Priority: 3
Q-values before update: [[15.090109 13.163398]]
Q-values after update: [[14.213831 12.637675]]
Episode 29 out of total 100, Total Reward: 11.0, Epsilon: 0.86, Current State: [-0.17607537 -1.7880524   0.22414017  2.7807853 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[7.1225886 6.091203 ]]
Q-values after update: [[6.92493  6.002608]]
Designated Priority: 1
Q-values before update: [[7.4674473 6.687539 ]]
Q-values after update: [[7.2395635 6.5729136]]
Designated Priority: 1
Q-values before update: [[7.8320465 7.1928487]]
Q-values after update: [[7.581511  7.0556874]]
Designated Priority: 1
Q-values before update: [[8.23516   7.6772738]]
Q-values after update: [[7.971475  7.5239577]]
Designated Priority: 1
Q-values before update: [[8.62378  8.148663]]
Q-values after update: [[8.3511   7.994178]]
Designated Priority: 1
Q-values before update: [[7.827613  7.4835167]]
Q-values after update: [[7.619362 7.367405]]
Designated Priority: 1
Q-values before update: [[8.235686 7.972822]]
Q-values after update: [[8.022358  7.8474326]]
Designated Priority: 1
Q-values before update: [[8.636267 8.454592]]
Q-values after update: [[8.423682 8.324055]]
Designated Priority: 1
Q-values before update: [[9.050872 8.942908]]
Q-values after update: [[8.841104 8.809437]]
Designated Priority: 1
Q-values before update: [[9.4727955 9.4373255]]
Q-values after update: [[9.2691965 9.30377  ]]
Designated Priority: 3
Q-values before update: [[9.920226 9.950521]]
Q-values after update: [[9.564608 9.391783]]
Episode 30 out of total 100, Total Reward: 11.0, Epsilon: 0.86, Current State: [-0.18064609 -1.3479636   0.24751692  2.2406452 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[5.8885036 5.5124454]]
Q-values after update: [[5.8089128 5.3420763]]
Designated Priority: 1
Q-values before update: [[5.999387 5.724127]]
Q-values after update: [[5.905218  5.5434055]]
Designated Priority: 1
Q-values before update: [[6.2090726 5.8839235]]
Q-values after update: [[6.104409  5.6968026]]
Designated Priority: 1
Q-values before update: [[6.4508   6.033164]]
Q-values after update: [[6.3392973 5.84297  ]]
Designated Priority: 1
Q-values before update: [[6.708299 6.183883]]
Q-values after update: [[6.593624  5.9944563]]
Designated Priority: 1
Q-values before update: [[6.979889 6.336373]]
Q-values after update: [[6.865592 6.150702]]
Designated Priority: 1
Q-values before update: [[7.272792 6.501718]]
Q-values after update: [[7.159895 6.322371]]
Designated Priority: 1
Q-values before update: [[7.5770216 6.674879 ]]
Q-values after update: [[7.4674516 6.502144 ]]
Designated Priority: 3
Q-values before update: [[7.8948708 6.855003 ]]
Q-values after update: [[7.6229415 6.5613346]]
Episode 31 out of total 100, Total Reward: 9.0, Epsilon: 0.86, Current State: [-0.13717216 -1.80469     0.23073141  2.846125  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[5.54766  4.584976]]
Q-values after update: [[5.491012 4.510648]]
Designated Priority: 1
Q-values before update: [[5.522571  4.7366657]]
Q-values after update: [[5.454862 4.654619]]
Designated Priority: 1
Q-values before update: [[5.5931487 4.827623 ]]
Q-values after update: [[5.516944  4.7401924]]
Designated Priority: 1
Q-values before update: [[5.73059   4.9167333]]
Q-values after update: [[5.649131 4.825712]]
Designated Priority: 1
Q-values before update: [[5.879542  5.0160656]]
Q-values after update: [[5.795417 4.923931]]
Designated Priority: 1
Q-values before update: [[6.038132  5.1012464]]
Q-values after update: [[5.949557  5.0010953]]
Designated Priority: 1
Q-values before update: [[6.2126493 5.1877985]]
Q-values after update: [[6.125608  5.0898786]]
Designated Priority: 3
Q-values before update: [[6.3967004 5.279883 ]]
Q-values after update: [[6.256151  5.0772257]]
Episode 32 out of total 100, Total Reward: 8.0, Epsilon: 0.85, Current State: [-0.08095998 -1.169804    0.21480893  1.9672643 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[5.090203 4.021724]]
Q-values after update: [[5.0620837 3.9560246]]
Designated Priority: 1
Q-values before update: [[4.988494  4.0747547]]
Q-values after update: [[4.953602 4.006062]]
Designated Priority: 1
Q-values before update: [[4.973651 4.075034]]
Q-values after update: [[4.933073  4.0045404]]
Designated Priority: 1
Q-values before update: [[5.036694  4.0557337]]
Q-values after update: [[4.9890795 3.9762151]]
Designated Priority: 1
Q-values before update: [[5.1132336 4.040657 ]]
Q-values after update: [[5.0643835 3.961602 ]]
Designated Priority: 1
Q-values before update: [[5.213789 4.03471 ]]
Q-values after update: [[5.1660666 3.9577496]]
Designated Priority: 1
Q-values before update: [[5.3489947 4.047669 ]]
Q-values after update: [[5.3030453 3.9733076]]
Designated Priority: 3
Q-values before update: [[5.495561 4.067549]]
Q-values after update: [[5.373511  3.9447162]]
Episode 33 out of total 100, Total Reward: 8.0, Epsilon: 0.85, Current State: [-0.14912222 -1.5762477   0.21685298  2.5286078 ], Steps Taken: 8
Designated Priority: 1
Q-values before update: [[5.0688014 3.6809123]]
Q-values after update: [[5.045001  3.6471705]]
Designated Priority: 1
Q-values before update: [[4.840133  3.6678956]]
Q-values after update: [[4.808398 3.626306]]
Designated Priority: 1
Q-values before update: [[4.6775994 3.5864122]]
Q-values after update: [[4.641778  3.5432615]]
Designated Priority: 1
Q-values before update: [[4.6179633 3.491684 ]]
Q-values after update: [[4.5793505 3.4478493]]
Designated Priority: 1
Q-values before update: [[4.574966  3.4073806]]
Q-values after update: [[4.5348673 3.3632438]]
Designated Priority: 1
Q-values before update: [[4.567352  3.3406975]]
Q-values after update: [[4.5271015 3.2971249]]
Designated Priority: 1
Q-values before update: [[4.5761247 3.283356 ]]
Q-values after update: [[4.5367327 3.241023 ]]
Designated Priority: 1
Q-values before update: [[4.6090646 3.2400272]]
Q-values after update: [[4.5719047 3.1997976]]
Designated Priority: 1
Q-values before update: [[4.6529727 3.2080555]]
Q-values after update: [[4.620492  3.1799235]]
Designated Priority: 1
Q-values before update: [[4.5974503 3.224014 ]]
Q-values after update: [[4.5739985 3.200652 ]]
Designated Priority: 3
Q-values before update: [[4.6884227 3.2243676]]
Q-values after update: [[4.595455  3.1562982]]
Episode 34 out of total 100, Total Reward: 11.0, Epsilon: 0.84, Current State: [-0.22514255 -1.7125093   0.24835853  2.7408292 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[4.8526235 3.43312  ]]
Q-values after update: [[4.83519   3.4169345]]
Designated Priority: 1
Q-values before update: [[4.588696 3.401849]]
Q-values after update: [[4.567259  3.3834407]]
Designated Priority: 1
Q-values before update: [[4.394611  3.3126576]]
Q-values after update: [[4.370402  3.2963703]]
Designated Priority: 1
Q-values before update: [[4.572202  3.3903673]]
Q-values after update: [[4.557393 3.379656]]
Designated Priority: 1
Q-values before update: [[4.3826623 3.3033357]]
Q-values after update: [[4.3646483 3.2911732]]
Designated Priority: 1
Q-values before update: [[4.3177924 3.2105887]]
Q-values after update: [[4.2985806 3.197451 ]]
Designated Priority: 1
Q-values before update: [[4.2658143 3.1296074]]
Q-values after update: [[4.245645 3.115684]]
Designated Priority: 1
Q-values before update: [[4.2446003 3.0639482]]
Q-values after update: [[4.224759 3.050127]]
Designated Priority: 1
Q-values before update: [[4.244425  3.0093968]]
Q-values after update: [[4.225724 2.996244]]
Designated Priority: 3
Q-values before update: [[4.2719135 2.9709246]]
Q-values after update: [[4.2009845 2.9232583]]
Episode 35 out of total 100, Total Reward: 10.0, Epsilon: 0.84, Current State: [-0.15602592 -1.5413793   0.21290179  2.5095475 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.7434564 3.3298082]]
Q-values after update: [[4.7303023 3.3273542]]
Designated Priority: 1
Q-values before update: [[5.1469593 3.2785118]]
Q-values after update: [[5.142824 3.280668]]
Designated Priority: 1
Q-values before update: [[4.723667  3.3245025]]
Q-values after update: [[4.716528 3.323361]]
Designated Priority: 1
Q-values before update: [[4.3898993 3.26161  ]]
Q-values after update: [[4.379491  3.2573469]]
Designated Priority: 1
Q-values before update: [[4.1300745 3.1370552]]
Q-values after update: [[4.1172333 3.130594 ]]
Designated Priority: 1
Q-values before update: [[3.9866319 3.0003989]]
Q-values after update: [[3.972564  2.9961064]]
Designated Priority: 1
Q-values before update: [[4.093885 3.124069]]
Q-values after update: [[4.0863047 3.1229503]]
Designated Priority: 1
Q-values before update: [[3.961472  2.9957826]]
Q-values after update: [[3.9523814 2.9936254]]
Designated Priority: 1
Q-values before update: [[3.8433394 2.874094 ]]
Q-values after update: [[3.833201  2.8708022]]
Designated Priority: 1
Q-values before update: [[3.7700145 2.775208 ]]
Q-values after update: [[3.7602658 2.7717745]]
Designated Priority: 1
Q-values before update: [[3.7158523 2.686554 ]]
Q-values after update: [[3.7071154 2.6834555]]
Designated Priority: 1
Q-values before update: [[3.6864393 2.6150334]]
Q-values after update: [[3.6800392 2.6131585]]
Designated Priority: 3
Q-values before update: [[3.6917424 2.6098096]]
Q-values after update: [[3.6410093 2.5806148]]
Episode 36 out of total 100, Total Reward: 13.0, Epsilon: 0.83, Current State: [-0.19039091 -1.7362221   0.22967663  2.7620816 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[4.75062  3.424518]]
Q-values after update: [[4.743971 3.421947]]
Designated Priority: 1
Q-values before update: [[4.3995514 3.3163018]]
Q-values after update: [[4.390675  3.3118253]]
Designated Priority: 1
Q-values before update: [[4.129715  3.1692824]]
Q-values after update: [[4.118795  3.1635609]]
Designated Priority: 1
Q-values before update: [[3.969052  3.0158403]]
Q-values after update: [[3.9569628 3.0093186]]
Designated Priority: 1
Q-values before update: [[3.8101623 2.8651373]]
Q-values after update: [[3.797166  2.8578303]]
Designated Priority: 1
Q-values before update: [[3.6981468 2.7384846]]
Q-values after update: [[3.685628  2.7312868]]
Designated Priority: 1
Q-values before update: [[3.603089  2.6209621]]
Q-values after update: [[3.5920808 2.6145492]]
Designated Priority: 1
Q-values before update: [[3.5337682 2.531493 ]]
Q-values after update: [[3.524594 2.526439]]
Designated Priority: 3
Q-values before update: [[3.489531  2.5011342]]
Q-values after update: [[3.4350805 2.4683325]]
Episode 37 out of total 100, Total Reward: 9.0, Epsilon: 0.83, Current State: [-0.16892102 -1.7523851   0.22325224  2.8224185 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[4.516237  3.2708511]]
Q-values after update: [[4.5087523 3.266222 ]]
Designated Priority: 1
Q-values before update: [[4.1206584 3.1315756]]
Q-values after update: [[4.1111236 3.1253974]]
Designated Priority: 1
Q-values before update: [[3.8118365 2.953874 ]]
Q-values after update: [[3.8003721 2.9466662]]
Designated Priority: 1
Q-values before update: [[3.5969121 2.7656546]]
Q-values after update: [[3.584168  2.7577276]]
Designated Priority: 1
Q-values before update: [[3.4005086 2.5865161]]
Q-values after update: [[3.3876584 2.5783803]]
Designated Priority: 1
Q-values before update: [[3.2432845 2.4287689]]
Q-values after update: [[3.2311802 2.4242744]]
Designated Priority: 1
Q-values before update: [[3.3296804 2.549842 ]]
Q-values after update: [[3.322751  2.5479972]]
Designated Priority: 1
Q-values before update: [[3.2002335 2.4109032]]
Q-values after update: [[3.1941466 2.4126668]]
Designated Priority: 1
Q-values before update: [[3.3235323 2.5551066]]
Q-values after update: [[3.3217318 2.5585146]]
Designated Priority: 1
Q-values before update: [[3.2099693 2.4283192]]
Q-values after update: [[3.2082484 2.4317675]]
Designated Priority: 1
Q-values before update: [[3.1196437 2.3163714]]
Q-values after update: [[3.1191468 2.3205216]]
Designated Priority: 3
Q-values before update: [[3.0505946 2.2429836]]
Q-values after update: [[3.0175388 2.2259111]]
Episode 38 out of total 100, Total Reward: 12.0, Epsilon: 0.83, Current State: [-0.21571209 -1.6097144   0.22975783  2.5165043 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.631278 3.320223]]
Q-values after update: [[4.628225  3.3198926]]
Designated Priority: 1
Q-values before update: [[4.1943665 3.1987975]]
Q-values after update: [[4.1900268 3.1974592]]
Designated Priority: 1
Q-values before update: [[3.846926  3.0121574]]
Q-values after update: [[3.8416464 3.0100806]]
Designated Priority: 1
Q-values before update: [[3.590845  2.8177204]]
Q-values after update: [[3.585161  2.8185458]]
Designated Priority: 1
Q-values before update: [[3.799082  2.9880564]]
Q-values after update: [[3.797703 2.990248]]
Designated Priority: 1
Q-values before update: [[3.5509064 2.8017085]]
Q-values after update: [[3.5485494 2.8036408]]
Designated Priority: 1
Q-values before update: [[3.3375556 2.6172662]]
Q-values after update: [[3.3355238 2.6191092]]
Designated Priority: 1
Q-values before update: [[3.1554337 2.44859  ]]
Q-values after update: [[3.1543171 2.4508069]]
Designated Priority: 1
Q-values before update: [[3.0253038 2.3108878]]
Q-values after update: [[3.0235045 2.3126242]]
Designated Priority: 1
Q-values before update: [[2.931343  2.2157443]]
Q-values after update: [[2.9310372 2.2179112]]
Designated Priority: 1
Q-values before update: [[2.8594427 2.179398 ]]
Q-values after update: [[2.86193   2.1831415]]
Designated Priority: 3
Q-values before update: [[2.8541594 2.1924207]]
Q-values after update: [[2.8211536 2.174275 ]]
Episode 39 out of total 100, Total Reward: 12.0, Epsilon: 0.82, Current State: [-0.20185237 -1.9523582   0.24831553  3.0144155 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.784699  3.4959576]]
Q-values after update: [[4.7836537 3.4962661]]
Designated Priority: 1
Q-values before update: [[4.340468  3.3526778]]
Q-values after update: [[4.339219  3.3569043]]
Designated Priority: 1
Q-values before update: [[4.7608094 3.474124 ]]
Q-values after update: [[4.7635446 3.4797316]]
Designated Priority: 1
Q-values before update: [[4.3131766 3.3387349]]
Q-values after update: [[4.3146853 3.3430765]]
Designated Priority: 1
Q-values before update: [[3.9669745 3.1520798]]
Q-values after update: [[3.9675615 3.1554134]]
Designated Priority: 1
Q-values before update: [[3.7043736 2.9490702]]
Q-values after update: [[3.7039561 2.951913 ]]
Designated Priority: 1
Q-values before update: [[3.4596822 2.7444475]]
Q-values after update: [[3.4596524 2.74711  ]]
Designated Priority: 1
Q-values before update: [[3.2473588 2.5568461]]
Q-values after update: [[3.2480073 2.5596616]]
Designated Priority: 1
Q-values before update: [[3.0704937 2.3890147]]
Q-values after update: [[3.070522  2.3913863]]
Designated Priority: 1
Q-values before update: [[2.926774 2.264168]]
Q-values after update: [[2.9281383 2.2668903]]
Designated Priority: 1
Q-values before update: [[2.816426  2.2014768]]
Q-values after update: [[2.8203347 2.2054572]]
Designated Priority: 3
Q-values before update: [[2.7555974 2.1771078]]
Q-values after update: [[2.743704  2.1576748]]
Episode 40 out of total 100, Total Reward: 12.0, Epsilon: 0.82, Current State: [-0.13216807 -1.568411    0.2267303   2.457261  ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.675841  3.4622376]]
Q-values after update: [[4.6804104 3.4606478]]
Designated Priority: 1
Q-values before update: [[4.2391834 3.3188682]]
Q-values after update: [[4.244049  3.3214626]]
Designated Priority: 1
Q-values before update: [[4.691836  3.4778783]]
Q-values after update: [[4.6989713 3.4817798]]
Designated Priority: 1
Q-values before update: [[4.2609944 3.3334928]]
Q-values after update: [[4.2673798 3.3366024]]
Designated Priority: 1
Q-values before update: [[3.9278865 3.1434188]]
Q-values after update: [[3.933509 3.145849]]
Designated Priority: 1
Q-values before update: [[3.695701  2.9399738]]
Q-values after update: [[3.701265 2.942072]]
Designated Priority: 1
Q-values before update: [[3.475877  2.7395873]]
Q-values after update: [[3.4823105 2.7417836]]
Designated Priority: 1
Q-values before update: [[3.2771053 2.5504937]]
Q-values after update: [[3.2848372 2.5532563]]
Designated Priority: 1
Q-values before update: [[3.1179738 2.383034 ]]
Q-values after update: [[3.1250153 2.3854527]]
Designated Priority: 1
Q-values before update: [[2.9888003 2.2544389]]
Q-values after update: [[2.9983852 2.258097 ]]
Designated Priority: 3
Q-values before update: [[2.8929536 2.18726  ]]
Q-values after update: [[2.863254  2.1660738]]
Episode 41 out of total 100, Total Reward: 11.0, Epsilon: 0.81, Current State: [-0.11915795 -1.8045539   0.25683314  2.8868814 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[4.86571   3.5172577]]
Q-values after update: [[4.8666253 3.5167506]]
Designated Priority: 1
Q-values before update: [[4.389185  3.3605144]]
Q-values after update: [[4.3888664 3.3591924]]
Designated Priority: 1
Q-values before update: [[3.998259 3.141749]]
Q-values after update: [[3.9968872 3.1395762]]
Designated Priority: 1
Q-values before update: [[3.6961522 2.9152162]]
Q-values after update: [[3.69361   2.9126768]]
Designated Priority: 1
Q-values before update: [[3.4345927 2.6881416]]
Q-values after update: [[3.4322605 2.6855085]]
Designated Priority: 1
Q-values before update: [[3.1960766 2.4719634]]
Q-values after update: [[3.194493  2.4696882]]
Designated Priority: 1
Q-values before update: [[2.9746037 2.2644775]]
Q-values after update: [[2.974803 2.263234]]
Designated Priority: 1
Q-values before update: [[2.776632  2.0916634]]
Q-values after update: [[2.7769916 2.0908792]]
Designated Priority: 1
Q-values before update: [[2.6274912 1.9954414]]
Q-values after update: [[2.6289477 1.9952835]]
Designated Priority: 3
Q-values before update: [[2.5383415 1.9405559]]
Q-values after update: [[2.5081131 1.9207994]]
Episode 42 out of total 100, Total Reward: 10.0, Epsilon: 0.81, Current State: [-0.1830279  -1.9396      0.23528337  3.0303934 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.839693  3.4882824]]
Q-values after update: [[4.8406587 3.4875803]]
Designated Priority: 1
Q-values before update: [[4.3683248 3.340001 ]]
Q-values after update: [[4.3680997 3.338568 ]]
Designated Priority: 1
Q-values before update: [[3.9592211 3.116274 ]]
Q-values after update: [[3.957977  3.1142676]]
Designated Priority: 1
Q-values before update: [[3.6577253 2.8857164]]
Q-values after update: [[3.655458 2.88363 ]]
Designated Priority: 1
Q-values before update: [[3.3974009 2.6568494]]
Q-values after update: [[3.3956146 2.654969 ]]
Designated Priority: 1
Q-values before update: [[3.148146 2.433477]]
Q-values after update: [[3.1484895 2.436312 ]]
Designated Priority: 1
Q-values before update: [[3.3999705 2.6581204]]
Q-values after update: [[3.4030728 2.6622083]]
Designated Priority: 1
Q-values before update: [[3.1663775 2.4481087]]
Q-values after update: [[3.1710718 2.4530935]]
Designated Priority: 1
Q-values before update: [[2.9595792 2.2520707]]
Q-values after update: [[2.9661198 2.2581918]]
Designated Priority: 3
Q-values before update: [[2.7666306 2.0780735]]
Q-values after update: [[2.7305593 2.0572438]]
Episode 43 out of total 100, Total Reward: 10.0, Epsilon: 0.81, Current State: [-0.16914985 -1.5611488   0.23624127  2.5312147 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.8869677 3.5476646]]
Q-values after update: [[4.884786  3.5466073]]
Designated Priority: 1
Q-values before update: [[4.3776298 3.3747773]]
Q-values after update: [[4.3733373 3.372105 ]]
Designated Priority: 1
Q-values before update: [[3.9647663 3.1438053]]
Q-values after update: [[3.9590664 3.140296 ]]
Designated Priority: 1
Q-values before update: [[3.6285782 2.8947818]]
Q-values after update: [[3.6222968 2.894688 ]]
Designated Priority: 1
Q-values before update: [[3.9208565 3.1209617]]
Q-values after update: [[3.919524  3.1225812]]
Designated Priority: 1
Q-values before update: [[3.5944612 2.8790305]]
Q-values after update: [[3.5917327 2.8802893]]
Designated Priority: 1
Q-values before update: [[3.307128  2.6339054]]
Q-values after update: [[3.305856  2.6388552]]
Designated Priority: 1
Q-values before update: [[3.5813198 2.8757977]]
Q-values after update: [[3.582703 2.881566]]
Designated Priority: 1
Q-values before update: [[3.309884  2.6433718]]
Q-values after update: [[3.3118565 2.6491659]]
Designated Priority: 1
Q-values before update: [[3.0456076 2.4170034]]
Q-values after update: [[3.048504 2.423163]]
Designated Priority: 1
Q-values before update: [[2.806763 2.203627]]
Q-values after update: [[2.8112862 2.2105956]]
Designated Priority: 3
Q-values before update: [[2.6083949 2.0333223]]
Q-values after update: [[2.5988522 2.019754 ]]
Episode 44 out of total 100, Total Reward: 12.0, Epsilon: 0.80, Current State: [-0.11294956 -1.2031852   0.22149712  1.9458929 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.8469906 3.538274 ]]
Q-values after update: [[4.8511615 3.5448372]]
Designated Priority: 1
Q-values before update: [[5.444698  3.6516278]]
Q-values after update: [[5.4512453 3.6592689]]
Designated Priority: 1
Q-values before update: [[4.876136  3.5767298]]
Q-values after update: [[4.882321 3.582572]]
Designated Priority: 1
Q-values before update: [[4.3960996 3.4022663]]
Q-values after update: [[4.401929  3.4063156]]
Designated Priority: 1
Q-values before update: [[3.9625297 3.161797 ]]
Q-values after update: [[3.967594 3.164771]]
Designated Priority: 1
Q-values before update: [[3.645895 2.911562]]
Q-values after update: [[3.6516092 2.9180186]]
Designated Priority: 1
Q-values before update: [[3.973282  3.1729865]]
Q-values after update: [[3.9812076 3.1803412]]
Designated Priority: 1
Q-values before update: [[3.6760356 2.9328523]]
Q-values after update: [[3.6834743 2.9397464]]
Designated Priority: 1
Q-values before update: [[3.4082673 2.6976779]]
Q-values after update: [[3.4167242 2.7046235]]
Designated Priority: 1
Q-values before update: [[3.1453495 2.463677 ]]
Q-values after update: [[3.1554534 2.4712024]]
Designated Priority: 1
Q-values before update: [[2.8933742 2.2345192]]
Q-values after update: [[2.9052446 2.242877 ]]
Designated Priority: 3
Q-values before update: [[2.6728075 2.0420458]]
Q-values after update: [[2.6462    2.0253823]]
Episode 45 out of total 100, Total Reward: 12.0, Epsilon: 0.80, Current State: [-0.15182635 -1.5897743   0.24557477  2.6273246 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[5.0640726 3.7234151]]
Q-values after update: [[5.0651555 3.72516  ]]
Designated Priority: 1
Q-values before update: [[4.5497446 3.5357242]]
Q-values after update: [[4.5497155 3.5358496]]
Designated Priority: 1
Q-values before update: [[4.111485  3.2788043]]
Q-values after update: [[4.110456  3.2778912]]
Designated Priority: 1
Q-values before update: [[3.7456713 3.0094929]]
Q-values after update: [[3.7433615 3.0081856]]
Designated Priority: 1
Q-values before update: [[3.429138  2.7360682]]
Q-values after update: [[3.4273176 2.734708 ]]
Designated Priority: 1
Q-values before update: [[3.1183355 2.467245 ]]
Q-values after update: [[3.1173792 2.4662285]]
Designated Priority: 1
Q-values before update: [[2.8361156 2.2131453]]
Q-values after update: [[2.8370032 2.2131147]]
Designated Priority: 1
Q-values before update: [[2.5800285 2.0021973]]
Q-values after update: [[2.5854692 2.0086398]]
Designated Priority: 1
Q-values before update: [[2.8180137 2.2004724]]
Q-values after update: [[2.8259122 2.2078516]]
Designated Priority: 3
Q-values before update: [[2.5785449 1.9939728]]
Q-values after update: [[2.54569   1.9762399]]
Episode 46 out of total 100, Total Reward: 10.0, Epsilon: 0.79, Current State: [-0.1209227  -1.5821201   0.24152932  2.5555365 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.9012575 3.5776317]]
Q-values after update: [[4.899544  3.5774055]]
Designated Priority: 1
Q-values before update: [[4.3512497 3.368658 ]]
Q-values after update: [[4.347825  3.3668532]]
Designated Priority: 1
Q-values before update: [[3.8668482 3.0833893]]
Q-values after update: [[3.862051  3.0806446]]
Designated Priority: 1
Q-values before update: [[3.4409118 2.7935822]]
Q-values after update: [[3.4352694 2.7905595]]
Designated Priority: 1
Q-values before update: [[3.0844502 2.4966538]]
Q-values after update: [[3.0784566 2.4936736]]
Designated Priority: 1
Q-values before update: [[2.76764   2.2246976]]
Q-values after update: [[2.7624273 2.2221634]]
Designated Priority: 1
Q-values before update: [[2.4867635 1.9749373]]
Q-values after update: [[2.4836884 1.9737298]]
Designated Priority: 1
Q-values before update: [[2.2778885 1.8241524]]
Q-values after update: [[2.2775261 1.8248907]]
Designated Priority: 1
Q-values before update: [[2.0759761 1.6943343]]
Q-values after update: [[2.079256  1.6972305]]
Designated Priority: 3
Q-values before update: [[1.9350784 1.6080756]]
Q-values after update: [[1.8936142 1.5853614]]
Episode 47 out of total 100, Total Reward: 10.0, Epsilon: 0.79, Current State: [-0.18612504 -1.9901673   0.21206327  2.9743145 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.915412  3.5743797]]
Q-values after update: [[4.9178157 3.5751035]]
Designated Priority: 1
Q-values before update: [[4.343581  3.3631957]]
Q-values after update: [[4.345543  3.3635151]]
Designated Priority: 1
Q-values before update: [[3.846988 3.077746]]
Q-values after update: [[3.8483126 3.077787 ]]
Designated Priority: 1
Q-values before update: [[3.4003057 2.7825077]]
Q-values after update: [[3.3935237 2.7819748]]
Designated Priority: 1
Q-values before update: [[3.7906592 3.039586 ]]
Q-values after update: [[3.795381  3.0442574]]
Designated Priority: 1
Q-values before update: [[3.3378382 2.746739 ]]
Q-values after update: [[3.340032  2.7502422]]
Designated Priority: 1
Q-values before update: [[2.9497783 2.4401321]]
Q-values after update: [[2.953495  2.4444337]]
Designated Priority: 1
Q-values before update: [[2.6186259 2.1594365]]
Q-values after update: [[2.6249633 2.1646698]]
Designated Priority: 1
Q-values before update: [[2.3682923 1.9351168]]
Q-values after update: [[2.3778956 1.9416171]]
Designated Priority: 1
Q-values before update: [[2.1536813 1.7754111]]
Q-values after update: [[2.1681304 1.7840394]]
Designated Priority: 1
Q-values before update: [[1.9356714 1.6363667]]
Q-values after update: [[1.9558665 1.6479442]]
Designated Priority: 3
Q-values before update: [[1.7729287 1.5377421]]
Q-values after update: [[1.7499155 1.5261464]]
Episode 48 out of total 100, Total Reward: 12.0, Epsilon: 0.79, Current State: [-0.17482856 -1.9997203   0.22226427  2.943123  ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[5.163614 3.76723 ]]
Q-values after update: [[5.168022  3.7697172]]
Designated Priority: 1
Q-values before update: [[4.618017 3.582634]]
Q-values after update: [[4.6225185 3.5852346]]
Designated Priority: 1
Q-values before update: [[4.1278815 3.3015718]]
Q-values after update: [[4.1319146 3.3039815]]
Designated Priority: 1
Q-values before update: [[3.6981    3.0140908]]
Q-values after update: [[3.7018678 3.016703 ]]
Designated Priority: 1
Q-values before update: [[3.316573  2.7080402]]
Q-values after update: [[3.3213382 2.7116504]]
Designated Priority: 1
Q-values before update: [[2.9389946 2.3991866]]
Q-values after update: [[2.9457664 2.4039652]]
Designated Priority: 1
Q-values before update: [[2.5915742 2.108358 ]]
Q-values after update: [[2.6005836 2.11446  ]]
Designated Priority: 1
Q-values before update: [[2.2714238 1.8696651]]
Q-values after update: [[2.284243  1.8775393]]
Designated Priority: 1
Q-values before update: [[1.9981683 1.6989486]]
Q-values after update: [[2.0156002 1.709202 ]]
Designated Priority: 3
Q-values before update: [[1.7923216 1.5752503]]
Q-values after update: [[1.7647468 1.5606977]]
Episode 49 out of total 100, Total Reward: 10.0, Epsilon: 0.78, Current State: [-0.13214919 -1.970121    0.25817266  3.0881722 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[5.329464 3.831846]]
Q-values after update: [[5.334033  3.8333945]]
Designated Priority: 1
Q-values before update: [[4.8031034 3.6750154]]
Q-values after update: [[4.807261  3.6765568]]
Designated Priority: 1
Q-values before update: [[4.285128  3.3863525]]
Q-values after update: [[4.2904205 3.3935802]]
Designated Priority: 1
Q-values before update: [[4.8074336 3.6793334]]
Q-values after update: [[4.81397  3.685966]]
Designated Priority: 1
Q-values before update: [[4.2929025 3.4017088]]
Q-values after update: [[4.299768  3.4086177]]
Designated Priority: 1
Q-values before update: [[3.8611867 3.1207082]]
Q-values after update: [[3.8675716 3.1272151]]
Designated Priority: 1
Q-values before update: [[3.5038822 2.836861 ]]
Q-values after update: [[3.5099213 2.8432827]]
Designated Priority: 1
Q-values before update: [[3.1212497 2.532359 ]]
Q-values after update: [[3.132973 2.546243]]
Designated Priority: 1
Q-values before update: [[3.5172617 2.8481028]]
Q-values after update: [[3.5277202 2.8599565]]
Designated Priority: 1
Q-values before update: [[3.1645546 2.5656235]]
Q-values after update: [[3.180924 2.580694]]
Designated Priority: 3
Q-values before update: [[2.8090494 2.2820876]]
Q-values after update: [[2.7571464 2.2579925]]
Episode 50 out of total 100, Total Reward: 11.0, Epsilon: 0.78, Current State: [-0.12787588 -1.3357986   0.21656144  2.2477324 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[5.184816  3.8192053]]
Q-values after update: [[5.181437  3.8198035]]
Designated Priority: 1
Q-values before update: [[4.642999  3.6259212]]
Q-values after update: [[4.6374683 3.6245143]]
Designated Priority: 1
Q-values before update: [[4.114052 3.326515]]
Q-values after update: [[4.106725  3.3239026]]
Designated Priority: 1
Q-values before update: [[3.6613624 3.0222764]]
Q-values after update: [[3.6496177 3.0177426]]
Designated Priority: 1
Q-values before update: [[3.2001395 2.683537 ]]
Q-values after update: [[3.1828122 2.677348 ]]
Designated Priority: 1
Q-values before update: [[2.7553256 2.3488054]]
Q-values after update: [[2.7401295 2.343896 ]]
Designated Priority: 1
Q-values before update: [[2.3274858 2.0238218]]
Q-values after update: [[2.316074  2.0210147]]
Designated Priority: 1
Q-values before update: [[1.9347054 1.7536994]]
Q-values after update: [[1.9286695 1.753332 ]]
Designated Priority: 3
Q-values before update: [[1.6134286 1.5638483]]
Q-values after update: [[1.5847433 1.5525922]]
Episode 51 out of total 100, Total Reward: 9.0, Epsilon: 0.77, Current State: [-0.12467346 -1.8019708   0.238622    2.849305  ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[5.082791 3.725953]]
Q-values after update: [[5.08476   3.7270057]]
Designated Priority: 1
Q-values before update: [[4.503003  3.5003083]]
Q-values after update: [[4.5043974 3.5008814]]
Designated Priority: 1
Q-values before update: [[3.9428928 3.1769793]]
Q-values after update: [[3.943332  3.1770372]]
Designated Priority: 1
Q-values before update: [[3.3852391 2.834117 ]]
Q-values after update: [[3.381993  2.8332345]]
Designated Priority: 1
Q-values before update: [[2.8704658 2.4754634]]
Q-values after update: [[2.8670938 2.4751506]]
Designated Priority: 1
Q-values before update: [[2.4287796 2.1453145]]
Q-values after update: [[2.4272785 2.1459696]]
Designated Priority: 1
Q-values before update: [[2.0181675 1.8346187]]
Q-values after update: [[2.0199797 1.8369491]]
Designated Priority: 1
Q-values before update: [[1.6853917 1.6226   ]]
Q-values after update: [[1.6914562 1.6267043]]
Designated Priority: 1
Q-values before update: [[1.3896707 1.4507887]]
Q-values after update: [[1.396251  1.4618733]]
Designated Priority: 1
Q-values before update: [[1.5882175 1.5461981]]
Q-values after update: [[1.6024141 1.5592334]]
Designated Priority: 3
Q-values before update: [[1.3356081 1.4083033]]
Q-values after update: [[1.3383993 1.4049317]]
Episode 52 out of total 100, Total Reward: 11.0, Epsilon: 0.77, Current State: [-0.2268685 -1.4187514  0.2533088  2.1999993], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[5.2267375 3.796273 ]]
Q-values after update: [[5.232632 3.797812]]
Designated Priority: 1
Q-values before update: [[4.6536345 3.5921197]]
Q-values after update: [[4.660461  3.5945275]]
Designated Priority: 1
Q-values before update: [[4.088874 3.269383]]
Q-values after update: [[4.0959883 3.2720017]]
Designated Priority: 1
Q-values before update: [[3.550251  2.9403276]]
Q-values after update: [[3.5604584 2.9443514]]
Designated Priority: 1
Q-values before update: [[3.0375597 2.5860808]]
Q-values after update: [[3.0499249 2.590795 ]]
Designated Priority: 1
Q-values before update: [[2.591927  2.2489734]]
Q-values after update: [[2.605009  2.2544217]]
Designated Priority: 1
Q-values before update: [[2.1880858 1.9365032]]
Q-values after update: [[2.2059405 1.9492482]]
Designated Priority: 1
Q-values before update: [[2.5558524 2.215064 ]]
Q-values after update: [[2.576447  2.2325335]]
Designated Priority: 1
Q-values before update: [[3.0040894 2.5450754]]
Q-values after update: [[3.0243542 2.5609188]]
Designated Priority: 1
Q-values before update: [[2.5914223 2.2367868]]
Q-values after update: [[2.6145813 2.2543766]]
Designated Priority: 1
Q-values before update: [[2.202735  1.9425405]]
Q-values after update: [[2.2292883 1.9619793]]
Designated Priority: 3
Q-values before update: [[1.8402538 1.6878245]]
Q-values after update: [[1.8274515 1.6854934]]
Episode 53 out of total 100, Total Reward: 12.0, Epsilon: 0.77, Current State: [-0.20894684 -1.5898613   0.2456037   2.517698  ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[5.2753363 3.873296 ]]
Q-values after update: [[5.278972  3.8763194]]
Designated Priority: 1
Q-values before update: [[4.7275424 3.6701696]]
Q-values after update: [[4.7315574 3.6734285]]
Designated Priority: 1
Q-values before update: [[4.176564  3.3595333]]
Q-values after update: [[4.1804094 3.3626895]]
Designated Priority: 1
Q-values before update: [[3.69296  3.049667]]
Q-values after update: [[3.6978297 3.0535045]]
Designated Priority: 1
Q-values before update: [[3.179445  2.7042701]]
Q-values after update: [[3.1858377 2.7089844]]
Designated Priority: 1
Q-values before update: [[2.724568  2.3711765]]
Q-values after update: [[2.7310019 2.3767967]]
Designated Priority: 1
Q-values before update: [[2.2966423 2.0537498]]
Q-values after update: [[2.3054097 2.0606081]]
Designated Priority: 1
Q-values before update: [[1.9064286 1.7906072]]
Q-values after update: [[1.9199493 1.7992892]]
Designated Priority: 1
Q-values before update: [[1.5583159 1.594368 ]]
Q-values after update: [[1.5787443 1.6061977]]
Designated Priority: 3
Q-values before update: [[1.3298476 1.4748755]]
Q-values after update: [[1.3342912 1.4677358]]
Episode 54 out of total 100, Total Reward: 10.0, Epsilon: 0.76, Current State: [-0.18300821 -1.6154755   0.2636738   2.5727336 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[5.652194  4.0659294]]
Q-values after update: [[5.6594644 4.0672483]]
Designated Priority: 1
Q-values before update: [[5.0970006 3.8753574]]
Q-values after update: [[5.1049757 3.8772354]]
Designated Priority: 1
Q-values before update: [[4.559113  3.5848868]]
Q-values after update: [[4.5681777 3.587657 ]]
Designated Priority: 1
Q-values before update: [[4.063058 3.279249]]
Q-values after update: [[4.072965 3.28246 ]]
Designated Priority: 1
Q-values before update: [[3.6074023 2.9554129]]
Q-values after update: [[3.622108  2.9606025]]
Designated Priority: 1
Q-values before update: [[3.131756  2.6162522]]
Q-values after update: [[3.1467662 2.622084 ]]
Designated Priority: 1
Q-values before update: [[2.6959116 2.2850735]]
Q-values after update: [[2.713843 2.292285]]
Designated Priority: 1
Q-values before update: [[2.2807837 1.9688741]]
Q-values after update: [[2.3024821 1.977902 ]]
Designated Priority: 1
Q-values before update: [[1.8831242 1.7255713]]
Q-values after update: [[1.9103564 1.736921 ]]
Designated Priority: 3
Q-values before update: [[1.5350411 1.5183003]]
Q-values after update: [[1.5261555 1.5110618]]
Episode 55 out of total 100, Total Reward: 10.0, Epsilon: 0.76, Current State: [-0.19182669 -1.9092858   0.24267213  3.0792048 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[5.803637  4.1640153]]
Q-values after update: [[5.810026  4.1654077]]
Designated Priority: 1
Q-values before update: [[5.2466507 3.9918516]]
Q-values after update: [[5.25332   3.9934335]]
Designated Priority: 1
Q-values before update: [[4.7372985 3.7185807]]
Q-values after update: [[4.7462707 3.7278628]]
Designated Priority: 1
Q-values before update: [[5.2426343 3.9867826]]
Q-values after update: [[5.2520204 3.9950342]]
Designated Priority: 1
Q-values before update: [[4.736165  3.7255974]]
Q-values after update: [[4.7485213 3.741507 ]]
Designated Priority: 1
Q-values before update: [[5.2519503 4.0016513]]
Q-values after update: [[5.265225 4.023505]]
Designated Priority: 1
Q-values before update: [[5.8213005 4.2155986]]
Q-values after update: [[5.835543  4.2367916]]
Designated Priority: 1
Q-values before update: [[5.289377 4.055073]]
Q-values after update: [[5.305018 4.082172]]
Designated Priority: 1
Q-values before update: [[5.856732  4.2867293]]
Q-values after update: [[5.8746495 4.3258176]]
Designated Priority: 1
Q-values before update: [[6.491692  4.4962068]]
Q-values after update: [[6.5107927 4.5347924]]
Designated Priority: 1
Q-values before update: [[5.9154615 4.3969903]]
Q-values after update: [[5.9351406 4.4424767]]
Designated Priority: 1
Q-values before update: [[6.543694 4.62104 ]]
Q-values after update: [[6.565024  4.6661763]]
Designated Priority: 1
Q-values before update: [[5.97641   4.5181565]]
Q-values after update: [[5.996115  4.5563436]]
Designated Priority: 1
Q-values before update: [[5.4696474 4.330502 ]]
Q-values after update: [[5.4887056 4.3620467]]
Designated Priority: 1
Q-values before update: [[4.9847674 4.091409 ]]
Q-values after update: [[5.0026503 4.118918 ]]
Designated Priority: 1
Q-values before update: [[4.5417624 3.8040469]]
Q-values after update: [[4.558895 3.828826]]
Designated Priority: 1
Q-values before update: [[4.149768 3.510742]]
Q-values after update: [[4.167729  3.5335577]]
Designated Priority: 1
Q-values before update: [[3.7059143 3.190324 ]]
Q-values after update: [[3.7254438 3.212751 ]]
Designated Priority: 1
Q-values before update: [[3.2906523 2.8732514]]
Q-values after update: [[3.3137808 2.8962092]]
Designated Priority: 3
Q-values before update: [[2.884734  2.5579352]]
Q-values after update: [[2.8078814 2.5205946]]
Episode 56 out of total 100, Total Reward: 20.0, Epsilon: 0.76, Current State: [-0.07479516 -1.5419315   0.23726445  2.687678  ], Steps Taken: 20
Designated Priority: 1
Q-values before update: [[5.766268 4.374162]]
Q-values after update: [[5.7666254 4.384955 ]]
Designated Priority: 1
Q-values before update: [[5.1769524 4.146934 ]]
Q-values after update: [[5.1746936 4.153068 ]]
Designated Priority: 1
Q-values before update: [[4.5971346 3.8156068]]
Q-values after update: [[4.590481  3.8164423]]
Designated Priority: 1
Q-values before update: [[4.02648   3.4489703]]
Q-values after update: [[4.0193534 3.45284  ]]
Designated Priority: 1
Q-values before update: [[4.540227  3.7809246]]
Q-values after update: [[4.542709  3.7952952]]
Designated Priority: 1
Q-values before update: [[5.0975676 4.106561 ]]
Q-values after update: [[5.1042037 4.1227703]]
Designated Priority: 1
Q-values before update: [[4.521122  3.7864056]]
Q-values after update: [[4.5262284 3.799243 ]]
Designated Priority: 1
Q-values before update: [[3.928962  3.4157264]]
Q-values after update: [[3.931308  3.4252791]]
Designated Priority: 1
Q-values before update: [[3.3668847 3.0266154]]
Q-values after update: [[3.3642585 3.032923 ]]
Designated Priority: 1
Q-values before update: [[2.7943342 2.6246152]]
Q-values after update: [[2.7933614 2.630261 ]]
Designated Priority: 1
Q-values before update: [[2.262726  2.2474687]]
Q-values after update: [[2.260485 2.252699]]
Designated Priority: 1
Q-values before update: [[1.8156182 1.9077189]]
Q-values after update: [[1.8182714 1.9201443]]
Designated Priority: 1
Q-values before update: [[2.1893318 2.2006075]]
Q-values after update: [[2.1987906 2.2199786]]
Designated Priority: 3
Q-values before update: [[2.7056713 2.579522 ]]
Q-values after update: [[2.6423628 2.5576696]]
Episode 57 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [-0.21508762 -1.1873828   0.21258143  1.85198   ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[6.1771493 4.829937 ]]
Q-values after update: [[6.170628  4.8356285]]
Designated Priority: 1
Q-values before update: [[5.5534463 4.5676036]]
Q-values after update: [[5.545314 4.570872]]
Designated Priority: 1
Q-values before update: [[4.95648  4.222543]]
Q-values after update: [[4.9451237 4.222421 ]]
Designated Priority: 1
Q-values before update: [[4.3264256 3.8259215]]
Q-values after update: [[4.3039527 3.8212547]]
Designated Priority: 1
Q-values before update: [[3.6634393 3.3946407]]
Q-values after update: [[3.6404164 3.3899705]]
Designated Priority: 1
Q-values before update: [[3.0270407 2.9631963]]
Q-values after update: [[3.0070455 2.959683 ]]
Designated Priority: 1
Q-values before update: [[2.4678059 2.5553362]]
Q-values after update: [[2.4574282 2.560587 ]]
Designated Priority: 1
Q-values before update: [[2.9279616 2.9036539]]
Q-values after update: [[2.922641 2.909606]]
Designated Priority: 1
Q-values before update: [[2.3900564 2.5140524]]
Q-values after update: [[2.3901145 2.5278177]]
Designated Priority: 1
Q-values before update: [[2.888254  2.8879883]]
Q-values after update: [[2.8922653 2.9013238]]
Designated Priority: 3
Q-values before update: [[2.3728554 2.5194979]]
Q-values after update: [[2.3407154 2.486025 ]]
Episode 58 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [-0.1570659  -0.932017    0.22396554  1.6471344 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[5.838451 4.648158]]
Q-values after update: [[5.836597 4.640377]]
Designated Priority: 1
Q-values before update: [[5.2099047 4.3651724]]
Q-values after update: [[5.206926 4.356924]]
Designated Priority: 1
Q-values before update: [[4.571543  3.9881752]]
Q-values after update: [[4.5660515 3.9780774]]
Designated Priority: 1
Q-values before update: [[3.862298  3.5464475]]
Q-values after update: [[3.8533645 3.5348973]]
Designated Priority: 1
Q-values before update: [[3.1980035 3.098284 ]]
Q-values after update: [[3.189659  3.0868373]]
Designated Priority: 1
Q-values before update: [[2.6053236 2.6611307]]
Q-values after update: [[2.601542  2.6558964]]
Designated Priority: 1
Q-values before update: [[3.1263769 3.0362628]]
Q-values after update: [[3.1267138 3.033934 ]]
Designated Priority: 1
Q-values before update: [[2.569635 2.621568]]
Q-values after update: [[2.574286  2.6255376]]
Designated Priority: 1
Q-values before update: [[3.103847  3.0132844]]
Q-values after update: [[3.1111016 3.0186722]]
Designated Priority: 3
Q-values before update: [[2.578521  2.6217153]]
Q-values after update: [[2.5502877 2.5839367]]
Episode 59 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.14943404 -0.805575    0.24006148  1.4475554 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[6.210207  4.8779197]]
Q-values after update: [[6.2090507 4.8645716]]
Designated Priority: 1
Q-values before update: [[5.5581317 4.5950017]]
Q-values after update: [[5.5565023 4.581967 ]]
Designated Priority: 1
Q-values before update: [[4.933935 4.215188]]
Q-values after update: [[4.9297795 4.200786 ]]
Designated Priority: 1
Q-values before update: [[4.221988  3.7649934]]
Q-values after update: [[4.2164726 3.7501428]]
Designated Priority: 1
Q-values before update: [[3.5357158 3.2948594]]
Q-values after update: [[3.5298114 3.2801275]]
Designated Priority: 1
Q-values before update: [[2.9170709 2.831892 ]]
Q-values after update: [[2.9148955 2.8240323]]
Designated Priority: 1
Q-values before update: [[3.4682808 3.2274778]]
Q-values after update: [[3.470738  3.2229905]]
Designated Priority: 1
Q-values before update: [[2.881     2.7838995]]
Q-values after update: [[2.8840556 2.7801888]]
Designated Priority: 3
Q-values before update: [[2.325606  2.3525953]]
Q-values after update: [[2.2820134 2.3215005]]
Episode 60 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.07132279 -1.3275421   0.22240381  2.2598994 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[5.855364  4.5991673]]
Q-values after update: [[5.8522987 4.593051 ]]
Designated Priority: 1
Q-values before update: [[5.2106886 4.2818847]]
Q-values after update: [[5.206735  4.2752504]]
Designated Priority: 1
Q-values before update: [[4.5097857 3.855656 ]]
Q-values after update: [[4.5026774 3.8465858]]
Designated Priority: 1
Q-values before update: [[3.7322166 3.3686385]]
Q-values after update: [[3.7196107 3.3576221]]
Designated Priority: 1
Q-values before update: [[3.024191  2.8814685]]
Q-values after update: [[3.0114925 2.8708029]]
Designated Priority: 1
Q-values before update: [[2.3809433 2.4041865]]
Q-values after update: [[2.3711262 2.4002333]]
Designated Priority: 1
Q-values before update: [[2.9321532 2.8125222]]
Q-values after update: [[2.9294333 2.811455 ]]
Designated Priority: 1
Q-values before update: [[2.3207633 2.3553896]]
Q-values after update: [[2.3209243 2.361023 ]]
Designated Priority: 3
Q-values before update: [[2.8849108 2.779401 ]]
Q-values after update: [[2.826303 2.749281]]
Episode 61 out of total 100, Total Reward: 9.0, Epsilon: 0.75, Current State: [-0.10939446 -1.0200344   0.23024507  1.7774926 ], Steps Taken: 9
Designated Priority: 1
Q-values before update: [[5.7176247 4.434035 ]]
Q-values after update: [[5.7068777 4.4286065]]
Designated Priority: 1
Q-values before update: [[5.0449057 4.1117334]]
Q-values after update: [[5.033062  4.1054006]]
Designated Priority: 1
Q-values before update: [[4.29493  3.656617]]
Q-values after update: [[4.270629  3.6435494]]
Designated Priority: 1
Q-values before update: [[3.4034176 3.1268039]]
Q-values after update: [[3.3775394 3.1134813]]
Designated Priority: 1
Q-values before update: [[2.622746  2.6145961]]
Q-values after update: [[2.5983338 2.6024625]]
Designated Priority: 1
Q-values before update: [[1.9135484 2.1166115]]
Q-values after update: [[1.892305  2.1112287]]
Designated Priority: 1
Q-values before update: [[2.495305  2.5315049]]
Q-values after update: [[2.4829206 2.5287683]]
Designated Priority: 1
Q-values before update: [[1.8085978 2.0496233]]
Q-values after update: [[1.7988007 2.0535488]]
Designated Priority: 1
Q-values before update: [[2.4035418 2.4790845]]
Q-values after update: [[2.4037578 2.489783 ]]
Designated Priority: 3
Q-values before update: [[3.0908368 2.9557202]]
Q-values after update: [[3.0098026 2.9255128]]
Episode 62 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [-0.1707907  -0.8297724   0.22952713  1.454505  ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[5.88625  4.586119]]
Q-values after update: [[5.868467  4.5958953]]
Designated Priority: 1
Q-values before update: [[6.6023655 4.829067 ]]
Q-values after update: [[6.593721  4.8421125]]
Designated Priority: 1
Q-values before update: [[5.8627973 4.6003056]]
Q-values after update: [[5.8512073 4.609096 ]]
Designated Priority: 1
Q-values before update: [[5.108888  4.2708883]]
Q-values after update: [[5.0973477 4.284066 ]]
Designated Priority: 1
Q-values before update: [[5.8305197 4.6037145]]
Q-values after update: [[5.8259306 4.620735 ]]
Designated Priority: 1
Q-values before update: [[5.073215 4.277878]]
Q-values after update: [[5.065201 4.288996]]
Designated Priority: 1
Q-values before update: [[4.1902757 3.770475 ]]
Q-values after update: [[4.1714835 3.774861 ]]
Designated Priority: 1
Q-values before update: [[3.2546034 3.236552 ]]
Q-values after update: [[3.2366161 3.239448 ]]
Designated Priority: 1
Q-values before update: [[2.4400294 2.7197125]]
Q-values after update: [[2.4280565 2.7271426]]
Designated Priority: 1
Q-values before update: [[3.1298707 3.1721754]]
Q-values after update: [[3.1234176 3.185476 ]]
Designated Priority: 1
Q-values before update: [[4.0067782 3.6870558]]
Q-values after update: [[4.0042973 3.700231 ]]
Designated Priority: 1
Q-values before update: [[3.0474195 3.1492786]]
Q-values after update: [[3.0472367 3.1663806]]
Designated Priority: 1
Q-values before update: [[3.9376233 3.673693 ]]
Q-values after update: [[3.9408684 3.690161 ]]
Designated Priority: 1
Q-values before update: [[2.979717  3.1385238]]
Q-values after update: [[2.9859364 3.1589844]]
Designated Priority: 1
Q-values before update: [[3.87123  3.668899]]
Q-values after update: [[3.8792992 3.68813  ]]
Designated Priority: 1
Q-values before update: [[2.9292936 3.1400993]]
Q-values after update: [[2.939259  3.1633487]]
Designated Priority: 1
Q-values before update: [[3.8053253 3.6722677]]
Q-values after update: [[3.8178456 3.6941006]]
Designated Priority: 1
Q-values before update: [[2.8968494 3.1526375]]
Q-values after update: [[2.9110198 3.17867  ]]
Designated Priority: 1
Q-values before update: [[3.743079  3.6854408]]
Q-values after update: [[3.760207  3.7098742]]
Designated Priority: 1
Q-values before update: [[2.8745756 3.1762018]]
Q-values after update: [[2.8930178 3.2051115]]
Designated Priority: 1
Q-values before update: [[3.681248  3.7084994]]
Q-values after update: [[3.705719  3.7421074]]
Designated Priority: 3
Q-values before update: [[4.621602  4.2706285]]
Q-values after update: [[4.518721 4.245765]]
Episode 63 out of total 100, Total Reward: 22.0, Epsilon: 0.75, Current State: [-0.14116837 -0.43199748  0.21888633  0.9444995 ], Steps Taken: 22
Designated Priority: 1
Q-values before update: [[5.832089  4.9654126]]
Q-values after update: [[5.7850566 4.9616985]]
Designated Priority: 1
Q-values before update: [[5.0361514 4.558292 ]]
Q-values after update: [[4.9669337 4.545493 ]]
Designated Priority: 1
Q-values before update: [[3.9866474 3.9954324]]
Q-values after update: [[3.930502 3.99205 ]]
Designated Priority: 1
Q-values before update: [[4.871914  4.5065084]]
Q-values after update: [[4.8201346 4.502835 ]]
Designated Priority: 1
Q-values before update: [[3.839441  3.9555666]]
Q-values after update: [[3.798382  3.9596293]]
Designated Priority: 1
Q-values before update: [[4.7337337 4.4733267]]
Q-values after update: [[4.6961875 4.4767737]]
Designated Priority: 1
Q-values before update: [[3.7148604 3.931819 ]]
Q-values after update: [[3.6860857 3.9417212]]
Designated Priority: 1
Q-values before update: [[4.6154127 4.4551444]]
Q-values after update: [[4.5927076 4.471753 ]]
Designated Priority: 1
Q-values before update: [[5.44797   4.9235787]]
Q-values after update: [[5.4393344 4.9521174]]
Designated Priority: 1
Q-values before update: [[6.271671 5.329044]]
Q-values after update: [[6.2648225 5.357899 ]]
Designated Priority: 1
Q-values before update: [[5.442057  5.0067606]]
Q-values after update: [[5.4344077 5.0396667]]
Designated Priority: 1
Q-values before update: [[6.260148 5.425957]]
Q-values after update: [[6.259056 5.460381]]
Designated Priority: 1
Q-values before update: [[5.425373  5.0931478]]
Q-values after update: [[5.4204535 5.120524 ]]
Designated Priority: 1
Q-values before update: [[4.502949  4.6297307]]
Q-values after update: [[4.5015   4.659285]]
Designated Priority: 1
Q-values before update: [[5.3899584 5.1492877]]
Q-values after update: [[5.3903337 5.1785736]]
Designated Priority: 1
Q-values before update: [[4.4657726 4.67912  ]]
Q-values after update: [[4.469397 4.710757]]
Designated Priority: 1
Q-values before update: [[5.3616085 5.209432 ]]
Q-values after update: [[5.3667693 5.2401605]]
Designated Priority: 1
Q-values before update: [[4.4333744 4.733628 ]]
Q-values after update: [[4.441394 4.766951]]
Designated Priority: 1
Q-values before update: [[5.33905  5.272543]]
Q-values after update: [[5.348376  5.3045483]]
Designated Priority: 1
Q-values before update: [[4.4037886 4.7925105]]
Q-values after update: [[4.415679  4.8272185]]
Designated Priority: 1
Q-values before update: [[5.312692 5.339565]]
Q-values after update: [[5.325738 5.372662]]
Designated Priority: 1
Q-values before update: [[4.376423  4.8555202]]
Q-values after update: [[4.3912354 4.8916245]]
Designated Priority: 1
Q-values before update: [[5.2851057 5.4114738]]
Q-values after update: [[5.301937 5.445912]]
Designated Priority: 1
Q-values before update: [[4.3610873 4.9249372]]
Q-values after update: [[4.379595  4.9630003]]
Designated Priority: 1
Q-values before update: [[5.256515  5.4889793]]
Q-values after update: [[5.2766924 5.531937 ]]
Designated Priority: 1
Q-values before update: [[6.1668496 6.043506 ]]
Q-values after update: [[6.189737 6.085669]]
Designated Priority: 1
Q-values before update: [[5.2633824 5.605507 ]]
Q-values after update: [[5.2844887 5.64959  ]]
Designated Priority: 1
Q-values before update: [[6.1703067 6.166941 ]]
Q-values after update: [[6.1964192 6.210864 ]]
Designated Priority: 1
Q-values before update: [[5.2759194 5.727511 ]]
Q-values after update: [[5.3021507 5.7673774]]
Designated Priority: 1
Q-values before update: [[4.4188366 5.239513 ]]
Q-values after update: [[4.4442973 5.2829804]]
Designated Priority: 1
Q-values before update: [[5.2762656 5.829328 ]]
Q-values after update: [[5.3053513 5.87926  ]]
Designated Priority: 3
Q-values before update: [[6.162299 6.405699]]
Q-values after update: [[6.1091313 6.2801743]]
Episode 64 out of total 100, Total Reward: 32.0, Epsilon: 0.75, Current State: [-0.08158339  0.35201037  0.21846952  0.2661767 ], Steps Taken: 32
Designated Priority: 1
Q-values before update: [[5.7993817 5.732595 ]]
Q-values after update: [[5.769328  5.6397295]]
Designated Priority: 1
Q-values before update: [[4.9520726 5.210496 ]]
Q-values after update: [[4.9283404 5.142661 ]]
Designated Priority: 1
Q-values before update: [[5.7284493 5.5709085]]
Q-values after update: [[5.708127 5.503296]]
Designated Priority: 1
Q-values before update: [[4.8801246 5.08007  ]]
Q-values after update: [[4.865242 5.03264 ]]
Designated Priority: 1
Q-values before update: [[5.6739483 5.4581356]]
Q-values after update: [[5.66119  5.410339]]
Designated Priority: 1
Q-values before update: [[4.8213296 4.9881153]]
Q-values after update: [[4.813397 4.956742]]
Designated Priority: 1
Q-values before update: [[5.6314845 5.384394 ]]
Q-values after update: [[5.624664 5.35226 ]]
Designated Priority: 1
Q-values before update: [[4.77161  4.926646]]
Q-values after update: [[4.7692485 4.902837 ]]
Designated Priority: 1
Q-values before update: [[3.806973 4.37831 ]]
Q-values after update: [[3.8090942 4.365982 ]]
Designated Priority: 1
Q-values before update: [[4.696864 4.856929]]
Q-values after update: [[4.7005186 4.848606 ]]
Designated Priority: 1
Q-values before update: [[5.547205 5.284746]]
Q-values after update: [[5.5514593 5.283557 ]]
Designated Priority: 1
Q-values before update: [[6.346805  5.6865025]]
Q-values after update: [[6.3514957 5.684427 ]]
Designated Priority: 1
Q-values before update: [[5.561599  5.3171988]]
Q-values after update: [[5.5694184 5.3172913]]
Designated Priority: 1
Q-values before update: [[4.6522446 4.880536 ]]
Q-values after update: [[4.662135 4.887752]]
Designated Priority: 1
Q-values before update: [[5.528286 5.323571]]
Q-values after update: [[5.5395494 5.330021 ]]
Designated Priority: 1
Q-values before update: [[4.612801  4.8938313]]
Q-values after update: [[4.626686 4.907192]]
Designated Priority: 1
Q-values before update: [[5.487097  5.3428345]]
Q-values after update: [[5.501557  5.3544784]]
Designated Priority: 1
Q-values before update: [[4.568916  4.9151134]]
Q-values after update: [[4.5856743 4.933265 ]]
Designated Priority: 1
Q-values before update: [[5.4417953 5.3733287]]
Q-values after update: [[5.460373 5.39672 ]]
Designated Priority: 1
Q-values before update: [[6.2852936 5.8462896]]
Q-values after update: [[6.2983212 5.8674717]]
Designated Priority: 1
Q-values before update: [[5.421835 5.451551]]
Q-values after update: [[5.4413595 5.479237 ]]
Designated Priority: 1
Q-values before update: [[6.309693  5.9359756]]
Q-values after update: [[6.3261304 5.9617314]]
Designated Priority: 1
Q-values before update: [[5.3971252 5.538203 ]]
Q-values after update: [[5.4180474 5.569417 ]]
Designated Priority: 1
Q-values before update: [[6.2898917 6.0252814]]
Q-values after update: [[6.311542  6.0551605]]
Designated Priority: 1
Q-values before update: [[5.394578 5.635137]]
Q-values after update: [[5.414846  5.6688323]]
Designated Priority: 3
Q-values before update: [[6.2585917 6.1232753]]
Q-values after update: [[6.1245365 6.09444  ]]
Episode 65 out of total 100, Total Reward: 26.0, Epsilon: 0.75, Current State: [-0.0115987  -0.04349285  0.2194426   0.8570989 ], Steps Taken: 26
Designated Priority: 1
Q-values before update: [[5.5638013 5.29709  ]]
Q-values after update: [[5.495856 5.281794]]
Designated Priority: 1
Q-values before update: [[4.709072 4.896427]]
Q-values after update: [[4.6374145 4.8867292]]
Designated Priority: 1
Q-values before update: [[5.417201  5.2728496]]
Q-values after update: [[5.366822  5.2668114]]
Designated Priority: 1
Q-values before update: [[4.544697 4.869384]]
Q-values after update: [[4.491168 4.867768]]
Designated Priority: 1
Q-values before update: [[5.3017592 5.266533 ]]
Q-values after update: [[5.2654467 5.267629 ]]
Designated Priority: 1
Q-values before update: [[4.4116735 4.857732 ]]
Q-values after update: [[4.3726583 4.862485 ]]
Designated Priority: 1
Q-values before update: [[5.2106433 5.2746043]]
Q-values after update: [[5.1839423 5.288508 ]]
Designated Priority: 1
Q-values before update: [[5.9853296 5.6603956]]
Q-values after update: [[5.9624214 5.675108 ]]
Designated Priority: 1
Q-values before update: [[5.138543 5.329605]]
Q-values after update: [[5.112796  5.3482966]]
Designated Priority: 1
Q-values before update: [[5.9401407 5.727696 ]]
Q-values after update: [[5.926165  5.7480836]]
Designated Priority: 1
Q-values before update: [[5.0793257 5.390292 ]]
Q-values after update: [[5.0629344 5.412879 ]]
Designated Priority: 1
Q-values before update: [[5.9113207 5.8001904]]
Q-values after update: [[5.9058547 5.8364086]]
Designated Priority: 1
Q-values before update: [[6.7524056 6.141105 ]]
Q-values after update: [[6.7492023 6.1783223]]
Designated Priority: 1
Q-values before update: [[5.9246387 5.916714 ]]
Q-values after update: [[5.923892 5.947537]]
Designated Priority: 1
Q-values before update: [[5.0478873 5.5676723]]
Q-values after update: [[5.0444345 5.597573 ]]
Designated Priority: 1
Q-values before update: [[5.9228973 5.9990883]]
Q-values after update: [[5.9274936 6.0421333]]
Designated Priority: 1
Q-values before update: [[6.782825  6.3672395]]
Q-values after update: [[6.791225 6.411994]]
Designated Priority: 1
Q-values before update: [[5.9668226 6.126921 ]]
Q-values after update: [[5.975266 6.173369]]
Designated Priority: 1
Q-values before update: [[6.8298116 6.503706 ]]
Q-values after update: [[6.846649  6.5728636]]
Designated Priority: 1
Q-values before update: [[7.6963315 6.9003873]]
Q-values after update: [[7.720113 6.971871]]
Designated Priority: 1
Q-values before update: [[6.9225116 6.6921897]]
Q-values after update: [[6.9440665 6.7703924]]
Designated Priority: 1
Q-values before update: [[7.814373  7.1113024]]
Q-values after update: [[7.8437653 7.1929417]]
Designated Priority: 1
Q-values before update: [[7.032161 6.887715]]
Q-values after update: [[7.0553474 6.954303 ]]
Designated Priority: 1
Q-values before update: [[6.2457633 6.6158442]]
Q-values after update: [[6.264651 6.676358]]
Designated Priority: 1
Q-values before update: [[7.12781   7.0401254]]
Q-values after update: [[7.1551046 7.1080093]]
Designated Priority: 1
Q-values before update: [[6.336238  6.7474823]]
Q-values after update: [[6.358323 6.810742]]
Designated Priority: 1
Q-values before update: [[7.2382183 7.19283  ]]
Q-values after update: [[7.2695827 7.2626934]]
Designated Priority: 1
Q-values before update: [[6.439355  6.8796153]]
Q-values after update: [[6.4669495 6.93597  ]]
Designated Priority: 1
Q-values before update: [[5.570713 6.467283]]
Q-values after update: [[5.593406  6.5174727]]
Designated Priority: 1
Q-values before update: [[6.5244   6.976165]]
Q-values after update: [[6.5541906 7.044004 ]]
Designated Priority: 1
Q-values before update: [[7.480573 7.46992 ]]
Q-values after update: [[7.5203433 7.5442023]]
Designated Priority: 1
Q-values before update: [[6.658142  7.1189094]]
Q-values after update: [[6.691384  7.1904674]]
Designated Priority: 1
Q-values before update: [[7.640446  7.6359773]]
Q-values after update: [[7.684497  7.7144766]]
Designated Priority: 1
Q-values before update: [[6.8100524 7.2676   ]]
Q-values after update: [[6.847194 7.343971]]
Designated Priority: 1
Q-values before update: [[7.8231177 7.8110967]]
Q-values after update: [[7.8718004 7.8949924]]
Designated Priority: 1
Q-values before update: [[6.9836316 7.425532 ]]
Q-values after update: [[7.0252833 7.508213 ]]
Designated Priority: 1
Q-values before update: [[8.032571  7.9995275]]
Q-values after update: [[8.086357 8.090411]]
Designated Priority: 1
Q-values before update: [[7.183249  7.5971775]]
Q-values after update: [[7.231925 7.673112]]
Designated Priority: 1
Q-values before update: [[6.368865  7.1662884]]
Q-values after update: [[6.409363 7.238095]]
Designated Priority: 1
Q-values before update: [[7.383494  7.7416587]]
Q-values after update: [[7.438699  7.8423443]]
Designated Priority: 1
Q-values before update: [[8.520435 8.39283 ]]
Q-values after update: [[8.587336 8.502678]]
Designated Priority: 1
Q-values before update: [[7.654232  7.9608426]]
Q-values after update: [[7.715897 8.076019]]
Designated Priority: 3
Q-values before update: [[8.82996  8.664041]]
Q-values after update: [[8.469004 8.53664 ]]
Episode 66 out of total 100, Total Reward: 43.0, Epsilon: 0.75, Current State: [ 0.11978354  0.18560776 -0.22287051 -0.8057978 ], Steps Taken: 43
Designated Priority: 1
Q-values before update: [[5.8572454 7.213611 ]]
Q-values after update: [[5.7284694 7.1869082]]
Designated Priority: 1
Q-values before update: [[6.6472554 7.840707 ]]
Q-values after update: [[6.4991903 7.817901 ]]
Designated Priority: 1
Q-values before update: [[7.3971705 8.384223 ]]
Q-values after update: [[7.22659  8.369839]]
Designated Priority: 1
Q-values before update: [[8.093205 8.894776]]
Q-values after update: [[7.9142675 8.893026 ]]
Designated Priority: 1
Q-values before update: [[8.723194 9.435316]]
Q-values after update: [[8.54543  9.459506]]
Designated Priority: 1
Q-values before update: [[ 9.346453 10.014742]]
Q-values after update: [[ 9.187121  10.0508175]]
Designated Priority: 1
Q-values before update: [[8.523595 9.594581]]
Q-values after update: [[8.40625  9.654199]]
Designated Priority: 1
Q-values before update: [[ 9.177814 10.216682]]
Q-values after update: [[ 9.080494 10.326609]]
Designated Priority: 1
Q-values before update: [[ 9.849936 10.90814 ]]
Q-values after update: [[ 9.783697 11.0903  ]]
Designated Priority: 3
Q-values before update: [[10.55862  11.702516]]
Q-values after update: [[ 9.883883 10.528771]]
Episode 67 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.14855552  1.597742   -0.21677849 -2.4776957 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.985735  6.9466033]]
Q-values after update: [[4.863831  6.6832976]]
Designated Priority: 1
Q-values before update: [[5.486566  7.1768274]]
Q-values after update: [[5.340062  6.8859587]]
Designated Priority: 1
Q-values before update: [[5.878562  7.1717625]]
Q-values after update: [[5.7061133 6.832946 ]]
Designated Priority: 1
Q-values before update: [[5.2467136 6.6584888]]
Q-values after update: [[5.1347423 6.4307785]]
Designated Priority: 1
Q-values before update: [[5.573144  6.5472226]]
Q-values after update: [[5.435621 6.288372]]
Designated Priority: 1
Q-values before update: [[5.843321 6.317406]]
Q-values after update: [[5.6840854 6.040404 ]]
Designated Priority: 1
Q-values before update: [[6.016319  6.0300574]]
Q-values after update: [[5.845757  5.7479825]]
Designated Priority: 1
Q-values before update: [[6.1487727 5.687605 ]]
Q-values after update: [[5.9715824 5.3990407]]
Designated Priority: 1
Q-values before update: [[5.7237625 5.4716053]]
Q-values after update: [[5.5896516 5.247178 ]]
Designated Priority: 1
Q-values before update: [[5.3458705 5.3241043]]
Q-values after update: [[5.247523 5.15269 ]]
Designated Priority: 1
Q-values before update: [[4.9806232 5.245578 ]]
Q-values after update: [[4.910685  5.1196513]]
Designated Priority: 1
Q-values before update: [[5.1093597 4.8586726]]
Q-values after update: [[5.031932 4.724538]]
Designated Priority: 1
Q-values before update: [[4.7919426 4.8307495]]
Q-values after update: [[4.739166 4.729776]]
Designated Priority: 3
Q-values before update: [[4.508098 4.847377]]
Q-values after update: [[4.429249 4.675227]]
Episode 68 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [ 0.14086379  0.39910817 -0.21811403 -0.9494318 ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[4.1662016 5.1804314]]
Q-values after update: [[4.133576  5.0959587]]
Designated Priority: 1
Q-values before update: [[4.464162  5.1009507]]
Q-values after update: [[4.422469 4.999495]]
Designated Priority: 1
Q-values before update: [[4.6133122 4.7290754]]
Q-values after update: [[4.5686736 4.6216426]]
Designated Priority: 1
Q-values before update: [[4.410922  4.9335637]]
Q-values after update: [[4.380488  4.8553195]]
Designated Priority: 1
Q-values before update: [[4.545774  4.5412745]]
Q-values after update: [[4.513825 4.458618]]
Designated Priority: 1
Q-values before update: [[4.3719163 4.7897778]]
Q-values after update: [[4.3503685 4.7299943]]
Designated Priority: 1
Q-values before update: [[4.490471  4.3760433]]
Q-values after update: [[4.4686046 4.313066 ]]
Designated Priority: 1
Q-values before update: [[4.338652 4.658007]]
Q-values after update: [[4.324418  4.6133204]]
Designated Priority: 1
Q-values before update: [[4.440621 4.223879]]
Q-values after update: [[4.423675 4.178233]]
Designated Priority: 1
Q-values before update: [[4.3043413 4.528485 ]]
Q-values after update: [[4.2980223 4.495275 ]]
Designated Priority: 1
Q-values before update: [[4.085752  4.7373924]]
Q-values after update: [[4.084621 4.717418]]
Designated Priority: 1
Q-values before update: [[4.2567782 4.3921957]]
Q-values after update: [[4.2533026 4.369907 ]]
Designated Priority: 1
Q-values before update: [[4.329396  3.9398243]]
Q-values after update: [[4.325111  3.9219017]]
Designated Priority: 1
Q-values before update: [[4.370974 3.489898]]
Q-values after update: [[4.371023  3.4822078]]
Designated Priority: 1
Q-values before update: [[4.421213 3.077153]]
Q-values after update: [[4.425887 3.072304]]
Designated Priority: 1
Q-values before update: [[4.3284945 3.3564255]]
Q-values after update: [[4.336419  3.3553855]]
Designated Priority: 1
Q-values before update: [[4.2279577 3.6396086]]
Q-values after update: [[4.237153  3.6405365]]
Designated Priority: 1
Q-values before update: [[4.133048  3.9286213]]
Q-values after update: [[4.1441765 3.9305487]]
Designated Priority: 1
Q-values before update: [[4.014681 4.219073]]
Q-values after update: [[4.0244446 4.2233214]]
Designated Priority: 1
Q-values before update: [[4.0303617 3.7003622]]
Q-values after update: [[4.042484  3.7069273]]
Designated Priority: 1
Q-values before update: [[3.908911  3.9811819]]
Q-values after update: [[3.9209406 3.9902987]]
Designated Priority: 1
Q-values before update: [[3.91001  3.460252]]
Q-values after update: [[3.9244633 3.4710634]]
Designated Priority: 3
Q-values before update: [[3.7906017 3.7139413]]
Q-values after update: [[3.761274  3.6965086]]
Episode 69 out of total 100, Total Reward: 23.0, Epsilon: 0.75, Current State: [ 0.13704216 -0.1887269  -0.21045911 -0.25482404], Steps Taken: 23
Designated Priority: 1
Q-values before update: [[4.165998 4.72541 ]]
Q-values after update: [[4.1499195 4.718598 ]]
Designated Priority: 1
Q-values before update: [[4.3741226 4.4469385]]
Q-values after update: [[4.357923  4.4426403]]
Designated Priority: 1
Q-values before update: [[4.4575686 4.0221796]]
Q-values after update: [[4.446537 4.018226]]
Designated Priority: 1
Q-values before update: [[4.335143 4.391965]]
Q-values after update: [[4.324874  4.3932824]]
Designated Priority: 1
Q-values before update: [[4.4153066 3.957057 ]]
Q-values after update: [[4.4102936 3.958998 ]]
Designated Priority: 1
Q-values before update: [[4.292562  4.3194237]]
Q-values after update: [[4.287373 4.325559]]
Designated Priority: 1
Q-values before update: [[4.368443  3.8744247]]
Q-values after update: [[4.368478  3.8813848]]
Designated Priority: 1
Q-values before update: [[4.242922  4.2256975]]
Q-values after update: [[4.243785 4.233935]]
Designated Priority: 1
Q-values before update: [[4.116289 4.555676]]
Q-values after update: [[4.122814  4.5633063]]
Designated Priority: 1
Q-values before update: [[3.8166919 4.566485 ]]
Q-values after update: [[3.8225284 4.5740466]]
Designated Priority: 1
Q-values before update: [[4.0693045 4.4395785]]
Q-values after update: [[4.0734725 4.4498916]]
Designated Priority: 1
Q-values before update: [[4.117585  3.9890716]]
Q-values after update: [[4.1252093 4.0012383]]
Designated Priority: 1
Q-values before update: [[4.0101633 4.3206477]]
Q-values after update: [[4.0172186 4.333402 ]]
Designated Priority: 1
Q-values before update: [[4.0591784 3.8554916]]
Q-values after update: [[4.0695953 3.8696568]]
Designated Priority: 1
Q-values before update: [[3.9382458 4.1695   ]]
Q-values after update: [[3.9476993 4.1843634]]
Designated Priority: 1
Q-values before update: [[3.9940512 3.700555 ]]
Q-values after update: [[4.0069017 3.71673  ]]
Designated Priority: 1
Q-values before update: [[3.8578176 3.995459 ]]
Q-values after update: [[3.869472  4.0125556]]
Designated Priority: 1
Q-values before update: [[3.9198523 3.5204248]]
Q-values after update: [[3.934865 3.538728]]
Designated Priority: 1
Q-values before update: [[3.765338  3.7935748]]
Q-values after update: [[3.7790852 3.8131454]]
Designated Priority: 1
Q-values before update: [[3.829199 3.31305 ]]
Q-values after update: [[3.846175  3.3342438]]
Designated Priority: 1
Q-values before update: [[3.6629195 3.5655797]]
Q-values after update: [[3.6785502 3.5882158]]
Designated Priority: 3
Q-values before update: [[3.7240105 3.0892704]]
Q-values after update: [[3.6885555 3.0728304]]
Episode 70 out of total 100, Total Reward: 22.0, Epsilon: 0.75, Current State: [ 0.07289443  0.0783574  -0.22730066 -0.74319273], Steps Taken: 22
Designated Priority: 1
Q-values before update: [[3.993466 4.640465]]
Q-values after update: [[3.9804995 4.6393175]]
Designated Priority: 1
Q-values before update: [[4.1636877 4.4284554]]
Q-values after update: [[4.1482544 4.428147 ]]
Designated Priority: 1
Q-values before update: [[4.2561874 4.002228 ]]
Q-values after update: [[4.2412877 4.001225 ]]
Designated Priority: 1
Q-values before update: [[4.105067 4.35025 ]]
Q-values after update: [[4.0959086 4.354312 ]]
Designated Priority: 1
Q-values before update: [[4.18928  3.909796]]
Q-values after update: [[4.181432  3.9136171]]
Designated Priority: 1
Q-values before update: [[4.0416956 4.2492   ]]
Q-values after update: [[4.037738  4.2570033]]
Designated Priority: 1
Q-values before update: [[4.1139526 3.7960107]]
Q-values after update: [[4.111214  3.8043754]]
Designated Priority: 1
Q-values before update: [[3.9699483 4.121805 ]]
Q-values after update: [[3.970106 4.133164]]
Designated Priority: 1
Q-values before update: [[4.0283685 3.6564627]]
Q-values after update: [[4.030401 3.668674]]
Designated Priority: 1
Q-values before update: [[3.8864994 3.9643655]]
Q-values after update: [[3.8902535 3.9791093]]
Designated Priority: 1
Q-values before update: [[3.9303193 3.486277 ]]
Q-values after update: [[3.9365754 3.5021763]]
Designated Priority: 1
Q-values before update: [[3.7886333 3.7717385]]
Q-values after update: [[3.7975793 3.787749 ]]
Designated Priority: 1
Q-values before update: [[3.6657522 4.055013 ]]
Q-values after update: [[3.6769805 4.071224 ]]
Designated Priority: 1
Q-values before update: [[3.502169  4.1934185]]
Q-values after update: [[3.5108907 4.2061563]]
Designated Priority: 1
Q-values before update: [[3.5361562 3.8112311]]
Q-values after update: [[3.5471797 3.8289285]]
Designated Priority: 3
Q-values before update: [[3.565762  3.3047438]]
Q-values after update: [[3.534032 3.288646]]
Episode 71 out of total 100, Total Reward: 16.0, Epsilon: 0.75, Current State: [ 0.02101394  0.00412336 -0.21235359 -0.62462556], Steps Taken: 16
Designated Priority: 1
Q-values before update: [[3.983731  4.7739873]]
Q-values after update: [[3.970372  4.7724533]]
Designated Priority: 1
Q-values before update: [[4.172654 4.653685]]
Q-values after update: [[4.1576767 4.651973 ]]
Designated Priority: 1
Q-values before update: [[4.2649393 4.261826 ]]
Q-values after update: [[4.251983 4.260132]]
Designated Priority: 1
Q-values before update: [[4.162013 4.66576 ]]
Q-values after update: [[4.1538014 4.668352 ]]
Designated Priority: 1
Q-values before update: [[4.2477045 4.2625313]]
Q-values after update: [[4.2397366 4.267982 ]]
Designated Priority: 1
Q-values before update: [[4.2778354 3.853616 ]]
Q-values after update: [[4.272    3.860403]]
Designated Priority: 1
Q-values before update: [[4.2281513 4.2418976]]
Q-values after update: [[4.226    4.253045]]
Designated Priority: 1
Q-values before update: [[4.2481318 3.8161485]]
Q-values after update: [[4.249095  3.8290288]]
Designated Priority: 1
Q-values before update: [[4.194698  4.1847095]]
Q-values after update: [[4.199812 4.198301]]
Designated Priority: 1
Q-values before update: [[4.0956273 4.5449758]]
Q-values after update: [[4.104109  4.5590425]]
Designated Priority: 1
Q-values before update: [[3.9875944 4.811869 ]]
Q-values after update: [[3.9940088 4.8238564]]
Designated Priority: 1
Q-values before update: [[4.039517  4.4416947]]
Q-values after update: [[4.048119  4.4573846]]
Designated Priority: 1
Q-values before update: [[4.084008  3.9899015]]
Q-values after update: [[4.0958133 4.00823  ]]
Designated Priority: 1
Q-values before update: [[3.982722 4.319646]]
Q-values after update: [[3.9938676 4.3376403]]
Designated Priority: 1
Q-values before update: [[4.0150595 3.8575876]]
Q-values after update: [[4.0298257 3.8783123]]
Designated Priority: 1
Q-values before update: [[3.9092805 4.163641 ]]
Q-values after update: [[3.9228   4.184102]]
Designated Priority: 1
Q-values before update: [[3.9298368 3.6917171]]
Q-values after update: [[3.9473176 3.7149506]]
Designated Priority: 1
Q-values before update: [[3.817852  3.9704614]]
Q-values after update: [[3.83647   3.9926388]]
Designated Priority: 1
Q-values before update: [[3.7144263 4.257022 ]]
Q-values after update: [[3.7295644 4.276222 ]]
Designated Priority: 1
Q-values before update: [[3.7105012 3.7430143]]
Q-values after update: [[3.7290044 3.768103 ]]
Designated Priority: 3
Q-values before update: [[3.7066855 3.2562544]]
Q-values after update: [[3.6646447 3.23351  ]]
Episode 72 out of total 100, Total Reward: 21.0, Epsilon: 0.75, Current State: [ 0.12036426  0.17248663 -0.22434735 -0.8767882 ], Steps Taken: 21
Designated Priority: 1
Q-values before update: [[4.216345 5.190677]]
Q-values after update: [[4.2034974 5.1901603]]
Designated Priority: 1
Q-values before update: [[4.469513 5.176358]]
Q-values after update: [[4.455007  5.1759806]]
Designated Priority: 1
Q-values before update: [[4.5617385 4.802409 ]]
Q-values after update: [[4.5448494 4.8022614]]
Designated Priority: 1
Q-values before update: [[4.5847225 4.4119787]]
Q-values after update: [[4.5696325 4.412574 ]]
Designated Priority: 1
Q-values before update: [[4.546835 4.811379]]
Q-values after update: [[4.5376635 4.817366 ]]
Designated Priority: 1
Q-values before update: [[4.5600767 4.4023685]]
Q-values after update: [[4.553828 4.409762]]
Designated Priority: 1
Q-values before update: [[4.52385   4.7900023]]
Q-values after update: [[4.5209174 4.8009906]]
Designated Priority: 1
Q-values before update: [[4.527328 4.364868]]
Q-values after update: [[4.5270863 4.3816137]]
Designated Priority: 1
Q-values before update: [[4.522184  3.9370852]]
Q-values after update: [[4.526388  3.9568453]]
Designated Priority: 1
Q-values before update: [[4.482215  4.2943354]]
Q-values after update: [[4.4903727 4.314481 ]]
Designated Priority: 1
Q-values before update: [[4.433871  4.6348243]]
Q-values after update: [[4.4421844 4.655426 ]]
Designated Priority: 1
Q-values before update: [[4.4146214 4.178889 ]]
Q-values after update: [[4.4276547 4.202968 ]]
Designated Priority: 1
Q-values before update: [[4.3530264 4.493494 ]]
Q-values after update: [[4.365402  4.5177584]]
Designated Priority: 1
Q-values before update: [[4.3286448 4.0251493]]
Q-values after update: [[4.3460135 4.053143 ]]
Designated Priority: 1
Q-values before update: [[4.250301  4.3099647]]
Q-values after update: [[4.2687225 4.336692 ]]
Designated Priority: 1
Q-values before update: [[4.1667857 4.5912623]]
Q-values after update: [[4.181899  4.6151853]]
Designated Priority: 3
Q-values before update: [[4.1271057 4.087792 ]]
Q-values after update: [[4.0800657 4.0600023]]
Episode 73 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [ 0.16969348  0.21715431 -0.20993112 -0.6426391 ], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[4.1222796 5.2156615]]
Q-values after update: [[4.1031747 5.211267 ]]
Designated Priority: 1
Q-values before update: [[4.3206725 5.180087 ]]
Q-values after update: [[4.3036127 5.1755652]]
Designated Priority: 1
Q-values before update: [[4.090052  5.2083507]]
Q-values after update: [[4.079196 5.209417]]
Designated Priority: 1
Q-values before update: [[4.280402  5.1549864]]
Q-values after update: [[4.271977  5.1565356]]
Designated Priority: 1
Q-values before update: [[4.0708613 5.206702 ]]
Q-values after update: [[4.0667048 5.212175 ]]
Designated Priority: 1
Q-values before update: [[4.251291 5.132406]]
Q-values after update: [[4.246057  5.1382527]]
Designated Priority: 1
Q-values before update: [[4.2908535 4.723867 ]]
Q-values after update: [[4.2841573 4.7297072]]
Designated Priority: 1
Q-values before update: [[4.264802  4.2960734]]
Q-values after update: [[4.258999  4.3060403]]
Designated Priority: 1
Q-values before update: [[4.2275624 3.858396 ]]
Q-values after update: [[4.2257547 3.87099  ]]
Designated Priority: 1
Q-values before update: [[4.203597  4.2118664]]
Q-values after update: [[4.205463  4.2290125]]
Designated Priority: 1
Q-values before update: [[4.153059  3.7511973]]
Q-values after update: [[4.15986   3.7719176]]
Designated Priority: 1
Q-values before update: [[4.1141534 4.0733013]]
Q-values after update: [[4.1248827 4.094729 ]]
Designated Priority: 1
Q-values before update: [[4.0653043 4.3766227]]
Q-values after update: [[4.075228 4.397409]]
Designated Priority: 1
Q-values before update: [[3.9996822 3.885588 ]]
Q-values after update: [[4.015397 3.910928]]
Designated Priority: 1
Q-values before update: [[3.9323933 4.15605  ]]
Q-values after update: [[3.9499617 4.181018 ]]
Designated Priority: 1
Q-values before update: [[3.8548748 4.407997 ]]
Q-values after update: [[3.869444 4.430151]]
Designated Priority: 3
Q-values before update: [[3.7797036 3.8965404]]
Q-values after update: [[3.74505   3.8182697]]
Episode 74 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [ 0.12212491  0.596382   -0.22661355 -1.2973862 ], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[4.059175  5.2560906]]
Q-values after update: [[4.0509496 5.2315917]]
Designated Priority: 1
Q-values before update: [[4.2492623 5.206437 ]]
Q-values after update: [[4.2379236 5.1739902]]
Designated Priority: 1
Q-values before update: [[4.275306  4.7432013]]
Q-values after update: [[4.2617707 4.7065997]]
Designated Priority: 1
Q-values before update: [[4.2319684 4.2542214]]
Q-values after update: [[4.2188377 4.2209234]]
Designated Priority: 1
Q-values before update: [[4.1755137 3.7463727]]
Q-values after update: [[4.1665635 3.7154639]]
Designated Priority: 1
Q-values before update: [[4.145573  4.0697017]]
Q-values after update: [[4.143207  4.0484514]]
Designated Priority: 1
Q-values before update: [[4.11161  4.389612]]
Q-values after update: [[4.1108694 4.3757844]]
Designated Priority: 1
Q-values before update: [[4.0393844 3.8522928]]
Q-values after update: [[4.0434623 3.8412528]]
Designated Priority: 1
Q-values before update: [[3.9925177 4.1562133]]
Q-values after update: [[3.9971745 4.1509633]]
Designated Priority: 1
Q-values before update: [[3.9123363 3.5999444]]
Q-values after update: [[3.922083  3.6035533]]
Designated Priority: 1
Q-values before update: [[3.8358884 3.068406 ]]
Q-values after update: [[3.8523557 3.0769205]]
Designated Priority: 3
Q-values before update: [[3.755757  3.3023212]]
Q-values after update: [[3.6948967 3.2505677]]
Episode 75 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [ 0.08315416  0.39429843 -0.21927005 -0.92628694], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.0550814 5.1630282]]
Q-values after update: [[4.043919  5.1522136]]
Designated Priority: 1
Q-values before update: [[3.7887287 5.110615 ]]
Q-values after update: [[3.782625  5.1067486]]
Designated Priority: 1
Q-values before update: [[4.0432916 5.162313 ]]
Q-values after update: [[4.036702 5.159405]]
Designated Priority: 1
Q-values before update: [[4.213666  5.0941253]]
Q-values after update: [[4.2005997 5.087374 ]]
Designated Priority: 1
Q-values before update: [[4.214132  4.6266007]]
Q-values after update: [[4.1975193 4.6180687]]
Designated Priority: 1
Q-values before update: [[4.144382  4.1515884]]
Q-values after update: [[4.1272197 4.145883 ]]
Designated Priority: 1
Q-values before update: [[4.0595646 3.658173 ]]
Q-values after update: [[4.045637 3.654636]]
Designated Priority: 1
Q-values before update: [[4.091837 4.089198]]
Q-values after update: [[4.0874057 4.0919905]]
Designated Priority: 1
Q-values before update: [[4.1265106 4.516096 ]]
Q-values after update: [[4.1250095 4.5217404]]
Designated Priority: 1
Q-values before update: [[4.02427   3.9908583]]
Q-values after update: [[4.027153  3.9998345]]
Designated Priority: 1
Q-values before update: [[4.0509987 4.3978286]]
Q-values after update: [[4.059094 4.409959]]
Designated Priority: 1
Q-values before update: [[4.052988 4.81823 ]]
Q-values after update: [[4.0603833 4.830043 ]]
Designated Priority: 1
Q-values before update: [[3.9657502 4.256552 ]]
Q-values after update: [[3.9745243 4.271146 ]]
Designated Priority: 1
Q-values before update: [[3.84938   3.7027965]]
Q-values after update: [[3.8634245 3.721518 ]]
Designated Priority: 1
Q-values before update: [[3.8526964 4.065796 ]]
Q-values after update: [[3.8657722 4.084817 ]]
Designated Priority: 1
Q-values before update: [[3.727329  3.4942045]]
Q-values after update: [[3.746054  3.5177264]]
Designated Priority: 1
Q-values before update: [[3.7097027 3.8232882]]
Q-values after update: [[3.7269056 3.8470113]]
Designated Priority: 1
Q-values before update: [[3.5762146 3.2346385]]
Q-values after update: [[3.599305 3.263128]]
Designated Priority: 3
Q-values before update: [[3.533517  3.5245364]]
Q-values after update: [[3.4966338 3.5001206]]
Episode 76 out of total 100, Total Reward: 19.0, Epsilon: 0.75, Current State: [ 0.1380447   0.20584805 -0.22253361 -0.70308775], Steps Taken: 19
Designated Priority: 1
Q-values before update: [[4.1510444 5.3462863]]
Q-values after update: [[4.1385384 5.343843 ]]
Designated Priority: 1
Q-values before update: [[4.2678413 5.2271304]]
Q-values after update: [[4.2526603 5.222705 ]]
Designated Priority: 1
Q-values before update: [[4.207936 4.701749]]
Q-values after update: [[4.191006  4.6973505]]
Designated Priority: 1
Q-values before update: [[4.087275  4.1735425]]
Q-values after update: [[4.071055 4.172409]]
Designated Priority: 1
Q-values before update: [[3.9513633 3.6269093]]
Q-values after update: [[3.939719 3.629182]]
Designated Priority: 1
Q-values before update: [[3.9595964 4.0031867]]
Q-values after update: [[3.956295 4.010283]]
Designated Priority: 1
Q-values before update: [[3.9670296 4.3709283]]
Q-values after update: [[3.9654198 4.3790545]]
Designated Priority: 1
Q-values before update: [[3.8162956 3.7950478]]
Q-values after update: [[3.8176544 3.8092804]]
Designated Priority: 1
Q-values before update: [[3.6586843 3.2173462]]
Q-values after update: [[3.6665907 3.242938 ]]
Designated Priority: 1
Q-values before update: [[3.4970448 2.6564317]]
Q-values after update: [[3.5148957 2.6908748]]
Designated Priority: 3
Q-values before update: [[3.4584339 2.9234798]]
Q-values after update: [[3.413149  2.8448799]]
Episode 77 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.10222705  1.0030594  -0.23167358 -1.7547075 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[4.049674 5.32179 ]]
Q-values after update: [[4.042633  5.3096275]]
Designated Priority: 1
Q-values before update: [[4.1839743 5.2659826]]
Q-values after update: [[4.1731744 5.2471704]]
Designated Priority: 1
Q-values before update: [[4.137337 4.751011]]
Q-values after update: [[4.123657  4.7266865]]
Designated Priority: 1
Q-values before update: [[4.0253477 4.206641 ]]
Q-values after update: [[4.0107183 4.181752 ]]
Designated Priority: 1
Q-values before update: [[3.8895192 3.6364093]]
Q-values after update: [[3.877877  3.6177359]]
Designated Priority: 1
Q-values before update: [[3.7415473 3.058126 ]]
Q-values after update: [[3.7366183 3.0428455]]
Designated Priority: 1
Q-values before update: [[3.7838557 3.4494345]]
Q-values after update: [[3.7862387 3.4433022]]
Designated Priority: 1
Q-values before update: [[3.8245819 3.8511896]]
Q-values after update: [[3.8291323 3.8524868]]
Designated Priority: 1
Q-values before update: [[3.654522  3.2179015]]
Q-values after update: [[3.6654248 3.2232263]]
Designated Priority: 1
Q-values before update: [[3.6747959 3.5899577]]
Q-values after update: [[3.6890109 3.599396 ]]
Designated Priority: 1
Q-values before update: [[3.6861014 3.9513419]]
Q-values after update: [[3.6983798 3.9621875]]
Designated Priority: 1
Q-values before update: [[3.5044858 3.290448 ]]
Q-values after update: [[3.5235875 3.30606  ]]
Designated Priority: 1
Q-values before update: [[3.4920628 3.618187 ]]
Q-values after update: [[3.5124853 3.635742 ]]
Designated Priority: 3
Q-values before update: [[3.4854147 3.956855 ]]
Q-values after update: [[3.461908 3.884395]]
Episode 78 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [ 0.12525928  0.39191958 -0.21972466 -0.9351449 ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[4.1138763 5.32899  ]]
Q-values after update: [[4.107744 5.299215]]
Designated Priority: 1
Q-values before update: [[4.238951  5.2083435]]
Q-values after update: [[4.2292895 5.1693697]]
Designated Priority: 1
Q-values before update: [[4.1901307 4.6338935]]
Q-values after update: [[4.1794724 4.5978127]]
Designated Priority: 1
Q-values before update: [[4.077639 4.052121]]
Q-values after update: [[4.0731573 4.0209346]]
Designated Priority: 1
Q-values before update: [[4.1482496 4.517493 ]]
Q-values after update: [[4.144747  4.4935675]]
Designated Priority: 1
Q-values before update: [[4.027386  3.9175086]]
Q-values after update: [[4.0301895 3.898552 ]]
Designated Priority: 1
Q-values before update: [[4.086466 4.370913]]
Q-values after update: [[4.0928874 4.3585434]]
Designated Priority: 1
Q-values before update: [[4.1193256 4.837713 ]]
Q-values after update: [[4.124816  4.8273554]]
Designated Priority: 1
Q-values before update: [[4.021445  4.2186317]]
Q-values after update: [[4.02888  4.213244]]
Designated Priority: 1
Q-values before update: [[3.8925493 3.5941107]]
Q-values after update: [[3.9060862 3.5935054]]
Designated Priority: 1
Q-values before update: [[3.923765 4.016499]]
Q-values after update: [[3.9354587 4.018927 ]]
Designated Priority: 1
Q-values before update: [[3.7878053 3.3752139]]
Q-values after update: [[3.8056278 3.382475 ]]
Designated Priority: 1
Q-values before update: [[3.796923  3.7689948]]
Q-values after update: [[3.8149166 3.7776134]]
Designated Priority: 1
Q-values before update: [[3.8122663 4.1618695]]
Q-values after update: [[3.8267846 4.1693273]]
Designated Priority: 1
Q-values before update: [[3.6574929 3.4998112]]
Q-values after update: [[3.6782203 3.5129168]]
Designated Priority: 1
Q-values before update: [[3.656031  3.8634272]]
Q-values after update: [[3.6730478 3.8758144]]
Designated Priority: 1
Q-values before update: [[3.4943457 3.1912775]]
Q-values after update: [[3.517632 3.208809]]
Designated Priority: 1
Q-values before update: [[3.463265  3.5219514]]
Q-values after update: [[3.4832146 3.53963  ]]
Designated Priority: 3
Q-values before update: [[3.303655  2.8373277]]
Q-values after update: [[3.2882016 2.784687 ]]
Episode 79 out of total 100, Total Reward: 19.0, Epsilon: 0.75, Current State: [ 0.107598    0.6229963  -0.22543375 -1.3510323 ], Steps Taken: 19
Designated Priority: 1
Q-values before update: [[4.150106 5.123217]]
Q-values after update: [[4.1494136 5.109    ]]
Designated Priority: 1
Q-values before update: [[4.2228928 4.8528953]]
Q-values after update: [[4.2196274 4.831739 ]]
Designated Priority: 1
Q-values before update: [[4.182126  4.2806053]]
Q-values after update: [[4.179288  4.2601247]]
Designated Priority: 1
Q-values before update: [[4.1000314 3.6886928]]
Q-values after update: [[4.101084 3.669588]]
Designated Priority: 1
Q-values before update: [[4.1303334 4.152715 ]]
Q-values after update: [[4.1334147 4.1428924]]
Designated Priority: 1
Q-values before update: [[4.0372157 3.5373757]]
Q-values after update: [[4.0447135 3.5296144]]
Designated Priority: 1
Q-values before update: [[4.0545526 3.9866536]]
Q-values after update: [[4.06275   3.9860413]]
Designated Priority: 1
Q-values before update: [[3.9518313 3.3496618]]
Q-values after update: [[3.9651437 3.351921 ]]
Designated Priority: 1
Q-values before update: [[3.9521794 3.777234 ]]
Q-values after update: [[3.9667056 3.78256  ]]
Designated Priority: 1
Q-values before update: [[3.9529057 4.2100697]]
Q-values after update: [[3.9649897 4.2174444]]
Designated Priority: 1
Q-values before update: [[3.839571 3.548598]]
Q-values after update: [[3.8570611 3.5588145]]
Designated Priority: 1
Q-values before update: [[3.8299341 3.9554434]]
Q-values after update: [[3.8449147 3.9672916]]
Designated Priority: 1
Q-values before update: [[3.70513   3.2824502]]
Q-values after update: [[3.7252963 3.2973998]]
Designated Priority: 1
Q-values before update: [[3.671443  3.6610625]]
Q-values after update: [[3.6891928 3.677745 ]]
Designated Priority: 1
Q-values before update: [[3.545393  2.9731305]]
Q-values after update: [[3.5687447 2.9933722]]
Designated Priority: 1
Q-values before update: [[3.483535  3.3177137]]
Q-values after update: [[3.5058532 3.337655 ]]
Designated Priority: 3
Q-values before update: [[3.4455523 3.6705003]]
Q-values after update: [[3.4318566 3.6173391]]
Episode 80 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [ 0.0941117   0.22512767 -0.2120345  -0.81430274], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[4.1876535 5.080132 ]]
Q-values after update: [[4.1842422 5.05521  ]]
Designated Priority: 1
Q-values before update: [[4.277887 4.79598 ]]
Q-values after update: [[4.2727914 4.7649145]]
Designated Priority: 1
Q-values before update: [[4.25646   4.1993184]]
Q-values after update: [[4.252829 4.175491]]
Designated Priority: 1
Q-values before update: [[4.1979704 3.5890052]]
Q-values after update: [[4.200488  3.5772545]]
Designated Priority: 1
Q-values before update: [[4.134196  2.9766932]]
Q-values after update: [[4.1440005 2.9715974]]
Designated Priority: 1
Q-values before update: [[4.1083198 3.3891718]]
Q-values after update: [[4.119013  3.3855953]]
Designated Priority: 1
Q-values before update: [[4.0781565 3.8086133]]
Q-values after update: [[4.0888395 3.8063707]]
Designated Priority: 1
Q-values before update: [[4.0535307 4.22562  ]]
Q-values after update: [[4.062466 4.224253]]
Designated Priority: 1
Q-values before update: [[3.9738598 3.5863667]]
Q-values after update: [[3.9877965 3.5903308]]
Designated Priority: 1
Q-values before update: [[3.937652 3.980973]]
Q-values after update: [[3.9490504 3.986093 ]]
Designated Priority: 1
Q-values before update: [[3.8511612 3.3328378]]
Q-values after update: [[3.8682303 3.3426368]]
Designated Priority: 1
Q-values before update: [[3.7923715 3.7043293]]
Q-values after update: [[3.8085313 3.7138457]]
Designated Priority: 1
Q-values before update: [[3.7495785 4.0976505]]
Q-values after update: [[3.7625487 4.1060195]]
Designated Priority: 1
Q-values before update: [[3.639311  3.4148178]]
Q-values after update: [[3.6575642 3.427924 ]]
Designated Priority: 1
Q-values before update: [[3.590139  3.7741933]]
Q-values after update: [[3.605396  3.7867565]]
Designated Priority: 1
Q-values before update: [[3.4757214 3.0968137]]
Q-values after update: [[3.4958792 3.1133687]]
Designated Priority: 1
Q-values before update: [[3.413678 3.41571 ]]
Q-values after update: [[3.4311378 3.4326644]]
Designated Priority: 3
Q-values before update: [[3.2929547 2.7427654]]
Q-values after update: [[3.2660496 2.7236857]]
Episode 81 out of total 100, Total Reward: 18.0, Epsilon: 0.75, Current State: [ 0.07712735 -0.00098587 -0.219238   -0.6102766 ], Steps Taken: 18
Designated Priority: 1
Q-values before update: [[4.4670477 5.2639513]]
Q-values after update: [[4.456571  5.2600007]]
Designated Priority: 1
Q-values before update: [[4.573304  4.9099994]]
Q-values after update: [[4.5616345 4.906116 ]]
Designated Priority: 1
Q-values before update: [[4.5666165 4.3605647]]
Q-values after update: [[4.556141 4.361743]]
Designated Priority: 1
Q-values before update: [[4.5301948 3.7922533]]
Q-values after update: [[4.522968  3.7956226]]
Designated Priority: 1
Q-values before update: [[4.4776583 4.230706 ]]
Q-values after update: [[4.4761806 4.2368326]]
Designated Priority: 1
Q-values before update: [[4.4381585 4.6780815]]
Q-values after update: [[4.4382415 4.686487 ]]
Designated Priority: 1
Q-values before update: [[4.3915987 4.0934553]]
Q-values after update: [[4.3955994 4.1043377]]
Designated Priority: 1
Q-values before update: [[4.3551908 4.523715 ]]
Q-values after update: [[4.3595853 4.536283 ]]
Designated Priority: 1
Q-values before update: [[4.2946687 3.9288964]]
Q-values after update: [[4.303252  3.9440136]]
Designated Priority: 1
Q-values before update: [[4.252351  4.3400135]]
Q-values after update: [[4.263541  4.3556995]]
Designated Priority: 1
Q-values before update: [[4.2164702 4.789184 ]]
Q-values after update: [[4.225288  4.8032517]]
Designated Priority: 1
Q-values before update: [[4.144509 4.155858]]
Q-values after update: [[4.156419 4.174461]]
Designated Priority: 1
Q-values before update: [[4.081138  3.5422723]]
Q-values after update: [[4.0971217 3.5637734]]
Designated Priority: 1
Q-values before update: [[4.0092916 3.9155493]]
Q-values after update: [[4.0246606 3.9384272]]
Designated Priority: 1
Q-values before update: [[3.9416153 3.2852592]]
Q-values after update: [[3.9616308 3.311465 ]]
Designated Priority: 1
Q-values before update: [[3.8487823 3.6275997]]
Q-values after update: [[3.8687303 3.6522279]]
Designated Priority: 1
Q-values before update: [[3.787566 3.97228 ]]
Q-values after update: [[3.8041697 3.9959884]]
Designated Priority: 1
Q-values before update: [[3.678327 3.319071]]
Q-values after update: [[3.700629  3.3507583]]
Designated Priority: 3
Q-values before update: [[3.614209 2.675652]]
Q-values after update: [[3.5611234 2.6490443]]
Episode 82 out of total 100, Total Reward: 19.0, Epsilon: 0.75, Current State: [ 0.14634766  0.24013935 -0.21814524 -0.84621435], Steps Taken: 19
Designated Priority: 1
Q-values before update: [[4.5322022 5.413058 ]]
Q-values after update: [[4.52422  5.412163]]
Designated Priority: 1
Q-values before update: [[4.2565   5.372551]]
Q-values after update: [[4.2531424 5.377098 ]]
Designated Priority: 1
Q-values before update: [[4.5298834 5.4345617]]
Q-values after update: [[4.5326366 5.4397416]]
Designated Priority: 1
Q-values before update: [[4.267859  5.4058456]]
Q-values after update: [[4.273472 5.415638]]
Designated Priority: 1
Q-values before update: [[4.551417 5.474065]]
Q-values after update: [[4.5561914 5.4844513]]
Designated Priority: 1
Q-values before update: [[4.7005353 5.3085155]]
Q-values after update: [[4.697593  5.3175526]]
Designated Priority: 1
Q-values before update: [[4.70373 4.80429]]
Q-values after update: [[4.698605 4.814987]]
Designated Priority: 1
Q-values before update: [[4.6600647 4.27764  ]]
Q-values after update: [[4.656387  4.2952366]]
Designated Priority: 1
Q-values before update: [[4.5981007 3.728231 ]]
Q-values after update: [[4.598379  3.7484322]]
Designated Priority: 1
Q-values before update: [[4.591198 4.194466]]
Q-values after update: [[4.5974984 4.2159758]]
Designated Priority: 1
Q-values before update: [[4.588892  4.6590457]]
Q-values after update: [[4.597185 4.682395]]
Designated Priority: 1
Q-values before update: [[4.516374 4.086131]]
Q-values after update: [[4.5283246 4.1121645]]
Designated Priority: 1
Q-values before update: [[4.5022864 4.524065 ]]
Q-values after update: [[4.5148606 4.551094 ]]
Designated Priority: 1
Q-values before update: [[4.4198294 3.9331627]]
Q-values after update: [[4.436822  3.9635358]]
Designated Priority: 1
Q-values before update: [[4.389755  4.3400683]]
Q-values after update: [[4.408635  4.3691216]]
Designated Priority: 1
Q-values before update: [[4.3936896 4.7512946]]
Q-values after update: [[4.409641  4.7773085]]
Designated Priority: 1
Q-values before update: [[4.2733927 4.1399045]]
Q-values after update: [[4.2950544 4.170286 ]]
Designated Priority: 1
Q-values before update: [[4.2600927 4.520668 ]]
Q-values after update: [[4.2828083 4.5495687]]
Designated Priority: 1
Q-values before update: [[4.241281  4.9382267]]
Q-values after update: [[4.2596216 4.9633517]]
Designated Priority: 1
Q-values before update: [[4.1208024 4.286473 ]]
Q-values after update: [[4.142264 4.315694]]
Designated Priority: 1
Q-values before update: [[4.0065837 3.660948 ]]
Q-values after update: [[4.0329905 3.6942575]]
Designated Priority: 1
Q-values before update: [[3.945006  3.9849164]]
Q-values after update: [[3.9690063 4.0171885]]
Designated Priority: 1
Q-values before update: [[3.828518  3.3424747]]
Q-values after update: [[3.857852 3.379116]]
Designated Priority: 3
Q-values before update: [[3.736442  3.6285858]]
Q-values after update: [[3.7007365 3.6080613]]
Episode 83 out of total 100, Total Reward: 24.0, Epsilon: 0.75, Current State: [ 0.17475383  0.04845013 -0.2199584  -0.5106142 ], Steps Taken: 24
Designated Priority: 1
Q-values before update: [[4.5003877 5.5324717]]
Q-values after update: [[4.485359  5.5299788]]
Designated Priority: 1
Q-values before update: [[4.5560865 5.316295 ]]
Q-values after update: [[4.5397124 5.312967 ]]
Designated Priority: 1
Q-values before update: [[4.507145 4.778059]]
Q-values after update: [[4.4905834 4.776899 ]]
Designated Priority: 1
Q-values before update: [[4.422122  4.2090173]]
Q-values after update: [[4.4093976 4.2105303]]
Designated Priority: 1
Q-values before update: [[4.3707857 4.5959606]]
Q-values after update: [[4.362528 4.601541]]
Designated Priority: 1
Q-values before update: [[4.2732964 4.0047903]]
Q-values after update: [[4.269435  4.0136056]]
Designated Priority: 1
Q-values before update: [[4.21263   4.3661013]]
Q-values after update: [[4.211422 4.377782]]
Designated Priority: 1
Q-values before update: [[4.1035366 3.753442 ]]
Q-values after update: [[4.1070814 3.768749 ]]
Designated Priority: 1
Q-values before update: [[4.0275145 4.0827355]]
Q-values after update: [[4.032526 4.100335]]
Designated Priority: 1
Q-values before update: [[3.9073863 3.4489887]]
Q-values after update: [[3.918849 3.478559]]
Designated Priority: 1
Q-values before update: [[3.7772536 2.807146 ]]
Q-values after update: [[3.8006988 2.857026 ]]
Designated Priority: 3
Q-values before update: [[3.6489592 2.2570298]]
Q-values after update: [[3.5490248 2.204764 ]]
Episode 84 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [ 0.1325201   0.7547369  -0.23300363 -1.5184299 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.6145015 5.7602334]]
Q-values after update: [[4.596344 5.759952]]
Designated Priority: 1
Q-values before update: [[4.6762457 5.5917735]]
Q-values after update: [[4.653582  5.5890784]]
Designated Priority: 1
Q-values before update: [[4.6000934 5.0609083]]
Q-values after update: [[4.5714912 5.0552516]]
Designated Priority: 1
Q-values before update: [[4.465125  4.4887853]]
Q-values after update: [[4.4330854 4.4850426]]
Designated Priority: 1
Q-values before update: [[4.298783  3.8812456]]
Q-values after update: [[4.268317  3.8789406]]
Designated Priority: 1
Q-values before update: [[4.2698536 4.2616158]]
Q-values after update: [[4.254302 4.267324]]
Designated Priority: 1
Q-values before update: [[4.257725 4.646805]]
Q-values after update: [[4.2489796 4.655697 ]]
Designated Priority: 1
Q-values before update: [[4.0738935 4.0103264]]
Q-values after update: [[4.06832  4.022646]]
Designated Priority: 1
Q-values before update: [[4.0547   4.367789]]
Q-values after update: [[4.053372  4.3819575]]
Designated Priority: 1
Q-values before update: [[3.8528585 3.7050662]]
Q-values after update: [[3.8556752 3.7234287]]
Designated Priority: 1
Q-values before update: [[3.8185995 4.027507 ]]
Q-values after update: [[3.8239074 4.047075 ]]
Designated Priority: 1
Q-values before update: [[3.6001163 3.3392503]]
Q-values after update: [[3.610184  3.3634968]]
Designated Priority: 3
Q-values before update: [[3.5434422 3.619262 ]]
Q-values after update: [[3.490649  3.5836399]]
Episode 85 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.12448896  0.23612677 -0.2141389  -0.6701694 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[4.3996553 5.744028 ]]
Q-values after update: [[4.380931  5.7401705]]
Designated Priority: 1
Q-values before update: [[4.5248966 5.7509785]]
Q-values after update: [[4.5048184 5.745908 ]]
Designated Priority: 1
Q-values before update: [[4.446228  5.2535157]]
Q-values after update: [[4.422453 5.245758]]
Designated Priority: 1
Q-values before update: [[4.2856393 4.702765 ]]
Q-values after update: [[4.2601576 4.6948957]]
Designated Priority: 1
Q-values before update: [[4.098958 4.112733]]
Q-values after update: [[4.0797224 4.1098704]]
Designated Priority: 1
Q-values before update: [[4.1628838 4.5661535]]
Q-values after update: [[4.1495185 4.567593 ]]
Designated Priority: 1
Q-values before update: [[3.956812 3.944124]]
Q-values after update: [[3.9504678 3.951445 ]]
Designated Priority: 1
Q-values before update: [[4.0108314 4.3690405]]
Q-values after update: [[4.0073204 4.378287 ]]
Designated Priority: 1
Q-values before update: [[3.7871995 3.7171888]]
Q-values after update: [[3.7913074 3.7330112]]
Designated Priority: 1
Q-values before update: [[3.8229914 4.1054   ]]
Q-values after update: [[3.827828  4.1217294]]
Designated Priority: 1
Q-values before update: [[3.583282  3.4254665]]
Q-values after update: [[3.5960934 3.448833 ]]
Designated Priority: 1
Q-values before update: [[3.5935187 3.7692878]]
Q-values after update: [[3.6057875 3.7926295]]
Designated Priority: 1
Q-values before update: [[3.338881  3.0627148]]
Q-values after update: [[3.3591504 3.093245 ]]
Designated Priority: 1
Q-values before update: [[3.316777  3.3545175]]
Q-values after update: [[3.3360527 3.3854172]]
Designated Priority: 3
Q-values before update: [[3.0481117 2.6227205]]
Q-values after update: [[3.0073423 2.5423732]]
Episode 86 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [ 0.1728189   0.9438157  -0.23477449 -1.7463821 ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[4.32464  5.733768]]
Q-values after update: [[4.3195524 5.722452 ]]
Designated Priority: 1
Q-values before update: [[4.371486 5.598331]]
Q-values after update: [[4.3687057 5.582014 ]]
Designated Priority: 1
Q-values before update: [[4.2908854 5.68109  ]]
Q-values after update: [[4.293029  5.6778913]]
Designated Priority: 1
Q-values before update: [[4.314809 5.484383]]
Q-values after update: [[4.3137007 5.4747496]]
Designated Priority: 1
Q-values before update: [[4.156226  4.8580794]]
Q-values after update: [[4.152516 4.844667]]
Designated Priority: 1
Q-values before update: [[3.9358141 4.184241 ]]
Q-values after update: [[3.931812 4.170273]]
Designated Priority: 1
Q-values before update: [[3.6913593 3.4620736]]
Q-values after update: [[3.6932657 3.451412 ]]
Designated Priority: 1
Q-values before update: [[3.7330697 3.8532174]]
Q-values after update: [[3.7377472 3.851097 ]]
Designated Priority: 1
Q-values before update: [[3.4671938 3.092827 ]]
Q-values after update: [[3.4781506 3.094792 ]]
Designated Priority: 1
Q-values before update: [[3.4820845 3.4459243]]
Q-values after update: [[3.4945452 3.4549847]]
Designated Priority: 1
Q-values before update: [[3.1977136 2.6560097]]
Q-values after update: [[3.2184622 2.6788135]]
Designated Priority: 3
Q-values before update: [[2.886996  1.9347509]]
Q-values after update: [[2.818991  1.8845747]]
Episode 87 out of total 100, Total Reward: 12.0, Epsilon: 0.75, Current State: [ 0.07234611  0.7864845  -0.22561821 -1.4922233 ], Steps Taken: 12
Designated Priority: 1
Q-values before update: [[4.4907417 5.87717  ]]
Q-values after update: [[4.4820657 5.8757005]]
Designated Priority: 1
Q-values before update: [[4.464248  5.6259685]]
Q-values after update: [[4.450842 5.618648]]
Designated Priority: 1
Q-values before update: [[4.2557855 4.95467  ]]
Q-values after update: [[4.2370353 4.9427376]]
Designated Priority: 1
Q-values before update: [[3.9832616 4.2304893]]
Q-values after update: [[3.961477  4.2172947]]
Designated Priority: 1
Q-values before update: [[3.6769874 3.4573905]]
Q-values after update: [[3.6595612 3.4475925]]
Designated Priority: 1
Q-values before update: [[3.7300775 3.8784974]]
Q-values after update: [[3.720012  3.8769982]]
Designated Priority: 1
Q-values before update: [[3.397935 3.066374]]
Q-values after update: [[3.3930323 3.0692146]]
Designated Priority: 1
Q-values before update: [[3.4322093 3.4494948]]
Q-values after update: [[3.4322567 3.4588091]]
Designated Priority: 1
Q-values before update: [[3.0770469 2.6049278]]
Q-values after update: [[3.0836418 2.6193523]]
Designated Priority: 3
Q-values before update: [[3.0825837 2.93523  ]]
Q-values after update: [[3.0213764 2.8854918]]
Episode 88 out of total 100, Total Reward: 10.0, Epsilon: 0.75, Current State: [ 0.09205969  0.42838514 -0.21582195 -0.8882586 ], Steps Taken: 10
Designated Priority: 1
Q-values before update: [[4.319371  5.7820067]]
Q-values after update: [[4.303317 5.776892]]
Designated Priority: 1
Q-values before update: [[4.3047123 5.5857735]]
Q-values after update: [[4.2838655 5.574069 ]]
Designated Priority: 1
Q-values before update: [[4.0597644 4.887899 ]]
Q-values after update: [[4.033786 4.871904]]
Designated Priority: 1
Q-values before update: [[3.7375183 4.1364512]]
Q-values after update: [[3.7082074 4.118294 ]]
Designated Priority: 1
Q-values before update: [[3.3792825 3.3304517]]
Q-values after update: [[3.356186  3.3177266]]
Designated Priority: 1
Q-values before update: [[3.486619  3.8052592]]
Q-values after update: [[3.4704201 3.798742 ]]
Designated Priority: 1
Q-values before update: [[3.1021643 2.9591527]]
Q-values after update: [[3.0930638 2.959031 ]]
Designated Priority: 1
Q-values before update: [[3.1917892 3.396039 ]]
Q-values after update: [[3.1935709 3.4046419]]
Designated Priority: 1
Q-values before update: [[3.2893207 3.831009 ]]
Q-values after update: [[3.2912836 3.8388326]]
Designated Priority: 1
Q-values before update: [[2.89178   2.9638147]]
Q-values after update: [[2.896063 2.976278]]
Designated Priority: 3
Q-values before update: [[2.4712822 2.0715594]]
Q-values after update: [[2.412102  2.0253267]]
Episode 89 out of total 100, Total Reward: 11.0, Epsilon: 0.75, Current State: [ 0.08026473  0.5800274  -0.21051838 -1.1811901 ], Steps Taken: 11
Designated Priority: 1
Q-values before update: [[4.3885446 5.9923615]]
Q-values after update: [[4.377864 5.991625]]
Designated Priority: 1
Q-values before update: [[4.449453  5.9414124]]
Q-values after update: [[4.4354014 5.9363146]]
Designated Priority: 1
Q-values before update: [[4.2267556 5.2906404]]
Q-values after update: [[4.2082877 5.28201  ]]
Designated Priority: 1
Q-values before update: [[3.9148908 4.5808125]]
Q-values after update: [[3.893177 4.570026]]
Designated Priority: 1
Q-values before update: [[3.5671191 3.821135 ]]
Q-values after update: [[3.5539622 3.8181465]]
Designated Priority: 1
Q-values before update: [[3.7836597 4.419507 ]]
Q-values after update: [[3.7752638 4.4200726]]
Designated Priority: 1
Q-values before update: [[3.413973 3.625146]]
Q-values after update: [[3.4058774 3.6279774]]
Designated Priority: 1
Q-values before update: [[3.0103834 2.7850947]]
Q-values after update: [[3.0124772 2.7973566]]
Designated Priority: 1
Q-values before update: [[3.1799557 3.3031805]]
Q-values after update: [[3.184574 3.318493]]
Designated Priority: 1
Q-values before update: [[2.7513666 2.4235044]]
Q-values after update: [[2.7664418 2.4486325]]
Designated Priority: 1
Q-values before update: [[2.8881793 2.8876302]]
Q-values after update: [[2.9107394 2.9180007]]
Designated Priority: 1
Q-values before update: [[3.0229263 3.3446603]]
Q-values after update: [[3.0416086 3.370717 ]]
Designated Priority: 1
Q-values before update: [[2.5815601 2.4364681]]
Q-values after update: [[2.6114259 2.4732604]]
Designated Priority: 3
Q-values before update: [[2.6759987 2.832915 ]]
Q-values after update: [[2.6411164 2.7563798]]
Episode 90 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [ 0.18378972  0.76735675 -0.21592672 -1.3673629 ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[4.409913  6.0749764]]
Q-values after update: [[4.405616 6.059312]]
Designated Priority: 1
Q-values before update: [[4.4733562 6.007107 ]]
Q-values after update: [[4.465048  5.9844594]]
Designated Priority: 1
Q-values before update: [[4.23654   5.3134503]]
Q-values after update: [[4.2251496 5.2848744]]
Designated Priority: 1
Q-values before update: [[3.913277  4.5543785]]
Q-values after update: [[3.9008708 4.5233135]]
Designated Priority: 1
Q-values before update: [[3.558064 3.741474]]
Q-values after update: [[3.5467455 3.7122324]]
Designated Priority: 1
Q-values before update: [[3.1686225 2.8761067]]
Q-values after update: [[3.1635752 2.8581479]]
Designated Priority: 1
Q-values before update: [[2.7321558 2.036801 ]]
Q-values after update: [[2.739701  2.0359218]]
Designated Priority: 1
Q-values before update: [[2.9109027 2.4679065]]
Q-values after update: [[2.9280474 2.4737728]]
Designated Priority: 1
Q-values before update: [[3.0718353 2.9647887]]
Q-values after update: [[3.088768 2.975904]]
Designated Priority: 1
Q-values before update: [[2.6302345 2.0469656]]
Q-values after update: [[2.659669  2.0698428]]
Designated Priority: 1
Q-values before update: [[2.7529423 2.4600933]]
Q-values after update: [[2.784435 2.485827]]
Designated Priority: 1
Q-values before update: [[2.8635144 2.8928819]]
Q-values after update: [[2.89628   2.9206705]]
Designated Priority: 3
Q-values before update: [[2.975457  3.3249056]]
Q-values after update: [[2.943873  3.2415106]]
Episode 91 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.16801165  0.5878671  -0.21038337 -1.072368  ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[4.464738 6.018541]]
Q-values after update: [[4.4584045 5.9909453]]
Designated Priority: 1
Q-values before update: [[4.4506903 5.7504973]]
Q-values after update: [[4.438995  5.7112284]]
Designated Priority: 1
Q-values before update: [[4.184856  4.9774494]]
Q-values after update: [[4.1727533 4.9362226]]
Designated Priority: 1
Q-values before update: [[3.8580778 4.1563826]]
Q-values after update: [[3.8473942 4.1168633]]
Designated Priority: 1
Q-values before update: [[3.5008059 3.2854362]]
Q-values after update: [[3.500138  3.2543547]]
Designated Priority: 1
Q-values before update: [[3.698464 3.863278]]
Q-values after update: [[3.698622  3.8406763]]
Designated Priority: 1
Q-values before update: [[3.3223965 2.957426 ]]
Q-values after update: [[3.3322654 2.943133 ]]
Designated Priority: 1
Q-values before update: [[3.4932914 3.5034668]]
Q-values after update: [[3.5024576 3.4955058]]
Designated Priority: 1
Q-values before update: [[3.1007833 2.5696359]]
Q-values after update: [[3.120391  2.5713532]]
Designated Priority: 1
Q-values before update: [[3.2375252 3.0690525]]
Q-values after update: [[3.259347 3.075062]]
Designated Priority: 1
Q-values before update: [[3.3733428 3.576483 ]]
Q-values after update: [[3.3964853 3.5863218]]
Designated Priority: 1
Q-values before update: [[3.538961 4.108817]]
Q-values after update: [[3.5625317 4.122134 ]]
Designated Priority: 1
Q-values before update: [[3.7038336 4.676753 ]]
Q-values after update: [[3.7205815 4.685592 ]]
Designated Priority: 1
Q-values before update: [[3.3085253 3.726853 ]]
Q-values after update: [[3.3289871 3.7388291]]
Designated Priority: 1
Q-values before update: [[2.9149618 2.7790413]]
Q-values after update: [[2.9451518 2.7994514]]
Designated Priority: 1
Q-values before update: [[3.0082877 3.234908 ]]
Q-values after update: [[3.0324845 3.2524867]]
Designated Priority: 3
Q-values before update: [[2.612799  2.2697458]]
Q-values after update: [[2.5913472 2.2451334]]
Episode 92 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [ 0.1359252   0.25912964 -0.21391425 -0.7439709 ], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[4.432954  5.8118296]]
Q-values after update: [[4.428612 5.808191]]
Designated Priority: 1
Q-values before update: [[4.374726 5.459512]]
Q-values after update: [[4.368229 5.452707]]
Designated Priority: 1
Q-values before update: [[4.1295967 4.687452 ]]
Q-values after update: [[4.121853 4.679925]]
Designated Priority: 1
Q-values before update: [[3.8216376 3.8740838]]
Q-values after update: [[3.821047  3.8728511]]
Designated Priority: 1
Q-values before update: [[3.9945772 4.4834905]]
Q-values after update: [[3.9948018 4.483734 ]]
Designated Priority: 1
Q-values before update: [[3.671456  3.6431916]]
Q-values after update: [[3.679302  3.6502335]]
Designated Priority: 1
Q-values before update: [[3.8282812 4.224271 ]]
Q-values after update: [[3.8350878 4.2312775]]
Designated Priority: 1
Q-values before update: [[3.490991  3.3580182]]
Q-values after update: [[3.5057142 3.3721478]]
Designated Priority: 1
Q-values before update: [[3.6253397 3.9036238]]
Q-values after update: [[3.6440709 3.9213233]]
Designated Priority: 1
Q-values before update: [[3.7825267 4.469594 ]]
Q-values after update: [[3.7966247 4.4836655]]
Designated Priority: 1
Q-values before update: [[3.434979  3.5926075]]
Q-values after update: [[3.4524477 3.6110775]]
Designated Priority: 1
Q-values before update: [[3.0784333 2.6858487]]
Q-values after update: [[3.1023827 2.7154121]]
Designated Priority: 1
Q-values before update: [[2.6610413 1.8535495]]
Q-values after update: [[2.6971557 1.8898113]]
Designated Priority: 1
Q-values before update: [[2.7437954 2.1708567]]
Q-values after update: [[2.7789524 2.2077413]]
Designated Priority: 3
Q-values before update: [[2.778274  2.5553608]]
Q-values after update: [[2.7555044 2.5396218]]
Episode 93 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [ 0.13359824  0.21559015 -0.21515332 -0.666264  ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[4.7139006 6.1128874]]
Q-values after update: [[4.7131314 6.113975 ]]
Designated Priority: 1
Q-values before update: [[4.5193667 6.1390057]]
Q-values after update: [[4.5209084 6.144965 ]]
Designated Priority: 1
Q-values before update: [[4.753044  6.1718574]]
Q-values after update: [[4.7554274 6.1805954]]
Designated Priority: 1
Q-values before update: [[4.826204  6.0587225]]
Q-values after update: [[4.8345947 6.070569 ]]
Designated Priority: 1
Q-values before update: [[4.784182 6.231874]]
Q-values after update: [[4.803979  6.2466702]]
Designated Priority: 1
Q-values before update: [[4.603086 6.277692]]
Q-values after update: [[4.6224985 6.295859 ]]
Designated Priority: 1
Q-values before update: [[4.8642845 6.3257995]]
Q-values after update: [[4.883658  6.3463464]]
Designated Priority: 1
Q-values before update: [[4.9981837 6.3100195]]
Q-values after update: [[5.012065 6.329873]]
Designated Priority: 1
Q-values before update: [[4.8468785 5.661006 ]]
Q-values after update: [[4.858661 5.68038 ]]
Designated Priority: 1
Q-values before update: [[4.6063085 4.951738 ]]
Q-values after update: [[4.62622  4.977784]]
Designated Priority: 1
Q-values before update: [[4.8312263 5.632788 ]]
Q-values after update: [[4.848916  5.6565704]]
Designated Priority: 1
Q-values before update: [[4.580882  4.9039097]]
Q-values after update: [[4.599042 4.929421]]
Designated Priority: 1
Q-values before update: [[4.3009086 4.131101 ]]
Q-values after update: [[4.327812  4.1641164]]
Designated Priority: 1
Q-values before update: [[4.476368  4.7351775]]
Q-values after update: [[4.5000167 4.765904 ]]
Designated Priority: 1
Q-values before update: [[4.180804 3.933905]]
Q-values after update: [[4.2134748 3.97253  ]]
Designated Priority: 1
Q-values before update: [[4.328377 4.495297]]
Q-values after update: [[4.3566713 4.5309124]]
Designated Priority: 1
Q-values before update: [[4.018633  3.6673756]]
Q-values after update: [[4.05595   3.7110171]]
Designated Priority: 1
Q-values before update: [[4.1327834 4.179617 ]]
Q-values after update: [[4.1653066 4.220348 ]]
Designated Priority: 1
Q-values before update: [[3.8097064 3.3262856]]
Q-values after update: [[3.8517778 3.3756528]]
Designated Priority: 1
Q-values before update: [[3.885959  3.7835705]]
Q-values after update: [[3.9273927 3.8305917]]
Designated Priority: 1
Q-values before update: [[3.9738224 4.2476053]]
Q-values after update: [[4.007608 4.287559]]
Designated Priority: 1
Q-values before update: [[3.639708  3.3784978]]
Q-values after update: [[3.6832628 3.4274702]]
Designated Priority: 1
Q-values before update: [[3.6863728 3.7865431]]
Q-values after update: [[3.7231894 3.8302805]]
Designated Priority: 3
Q-values before update: [[3.3471415 2.9000247]]
Q-values after update: [[3.2961845 2.861881 ]]
Episode 94 out of total 100, Total Reward: 24.0, Epsilon: 0.75, Current State: [ 0.20638743  0.44954455 -0.21214448 -0.80435294], Steps Taken: 24
Designated Priority: 1
Q-values before update: [[4.863551  6.3540463]]
Q-values after update: [[4.853701  6.3546033]]
Designated Priority: 1
Q-values before update: [[4.9427147 6.2530227]]
Q-values after update: [[4.9298906 6.249881 ]]
Designated Priority: 1
Q-values before update: [[4.755922  5.5870094]]
Q-values after update: [[4.739086  5.5815578]]
Designated Priority: 1
Q-values before update: [[4.4974513 4.8680315]]
Q-values after update: [[4.478469  4.8620415]]
Designated Priority: 1
Q-values before update: [[4.198245 4.094384]]
Q-values after update: [[4.186641  4.0948877]]
Designated Priority: 1
Q-values before update: [[4.3159237 4.633313 ]]
Q-values after update: [[4.309073 4.637845]]
Designated Priority: 1
Q-values before update: [[3.9940794 3.8230345]]
Q-values after update: [[3.9952214 3.8347929]]
Designated Priority: 1
Q-values before update: [[4.096044  4.3272114]]
Q-values after update: [[4.099083  4.3407545]]
Designated Priority: 1
Q-values before update: [[3.7533848 3.4825509]]
Q-values after update: [[3.764732  3.5037532]]
Designated Priority: 1
Q-values before update: [[3.8303406 3.942163 ]]
Q-values after update: [[3.841817 3.964093]]
Designated Priority: 1
Q-values before update: [[3.4681776 3.064818 ]]
Q-values after update: [[3.4872477 3.100577 ]]
Designated Priority: 1
Q-values before update: [[3.047777  2.2363057]]
Q-values after update: [[3.0816538 2.2774115]]
Designated Priority: 1
Q-values before update: [[3.0803747 2.5003567]]
Q-values after update: [[3.1134796 2.5454943]]
Designated Priority: 3
Q-values before update: [[3.0762572 2.8252206]]
Q-values after update: [[3.026246  2.7897274]]
Episode 95 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [ 0.17977108  0.40219668 -0.21506555 -0.819616  ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[4.8540015 6.4392433]]
Q-values after update: [[4.8415155 6.4390035]]
Designated Priority: 1
Q-values before update: [[4.9399943 6.3863087]]
Q-values after update: [[4.9256997 6.383753 ]]
Designated Priority: 1
Q-values before update: [[4.729589  5.7151866]]
Q-values after update: [[4.711927 5.710049]]
Designated Priority: 1
Q-values before update: [[4.4378705 4.983154 ]]
Q-values after update: [[4.417909  4.9770584]]
Designated Priority: 1
Q-values before update: [[4.1054296 4.193041 ]]
Q-values after update: [[4.086764  4.1914372]]
Designated Priority: 1
Q-values before update: [[3.7301488 3.3456368]]
Q-values after update: [[3.7204885 3.3522763]]
Designated Priority: 1
Q-values before update: [[3.8101604 3.801467 ]]
Q-values after update: [[3.8062875 3.8144405]]
Designated Priority: 1
Q-values before update: [[3.407674 2.91171 ]]
Q-values after update: [[3.4137661 2.9333441]]
Designated Priority: 1
Q-values before update: [[3.4582832 3.3129115]]
Q-values after update: [[3.4723394 3.3395684]]
Designated Priority: 1
Q-values before update: [[3.5157707 3.7171738]]
Q-values after update: [[3.5281878 3.7415051]]
Designated Priority: 1
Q-values before update: [[3.104525  2.8029127]]
Q-values after update: [[3.126625  2.8366709]]
Designated Priority: 1
Q-values before update: [[3.1222441 3.1438715]]
Q-values after update: [[3.1425004 3.176354 ]]
Designated Priority: 3
Q-values before update: [[2.6955743 2.2162786]]
Q-values after update: [[2.635293  2.1727567]]
Episode 96 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.14798118  0.60100937 -0.22225134 -1.1297534 ], Steps Taken: 13
Designated Priority: 1
Q-values before update: [[4.852887 6.565053]]
Q-values after update: [[4.8409514 6.564731 ]]
Designated Priority: 1
Q-values before update: [[4.8661127 6.4007134]]
Q-values after update: [[4.850567 6.396079]]
Designated Priority: 1
Q-values before update: [[4.6193757 5.7153363]]
Q-values after update: [[4.6102605 5.7163324]]
Designated Priority: 1
Q-values before update: [[4.799623  6.3299856]]
Q-values after update: [[4.7959213 6.3352175]]
Designated Priority: 1
Q-values before update: [[4.5429006 5.6315527]]
Q-values after update: [[4.5366044 5.635085 ]]
Designated Priority: 1
Q-values before update: [[4.2119923 4.873618 ]]
Q-values after update: [[4.2032776 4.875937 ]]
Designated Priority: 1
Q-values before update: [[3.8386738 4.05592  ]]
Q-values after update: [[3.830004  4.0605597]]
Designated Priority: 1
Q-values before update: [[3.4196677 3.1768496]]
Q-values after update: [[3.4212265 3.1912825]]
Designated Priority: 1
Q-values before update: [[3.5146816 3.6126482]]
Q-values after update: [[3.5194354 3.6305914]]
Designated Priority: 1
Q-values before update: [[3.0672824 2.6895733]]
Q-values after update: [[3.0826988 2.717877 ]]
Designated Priority: 1
Q-values before update: [[3.126844  3.0659647]]
Q-values after update: [[3.150086 3.099395]]
Designated Priority: 1
Q-values before update: [[3.1924038 3.4450362]]
Q-values after update: [[3.2123039 3.474519 ]]
Designated Priority: 1
Q-values before update: [[2.7366252 2.4996736]]
Q-values after update: [[2.7672207 2.5397882]]
Designated Priority: 3
Q-values before update: [[2.7572885 2.8105745]]
Q-values after update: [[2.7134006 2.7205043]]
Episode 97 out of total 100, Total Reward: 14.0, Epsilon: 0.75, Current State: [ 0.18933704  0.80745095 -0.21704061 -1.4018207 ], Steps Taken: 14
Designated Priority: 1
Q-values before update: [[4.7654085 6.556692 ]]
Q-values after update: [[4.7609105 6.54061  ]]
Designated Priority: 1
Q-values before update: [[4.902959  6.5804524]]
Q-values after update: [[4.9053097 6.5664587]]
Designated Priority: 1
Q-values before update: [[4.8051662 6.575442 ]]
Q-values after update: [[4.810721  6.5720124]]
Designated Priority: 1
Q-values before update: [[4.9420424 6.6062407]]
Q-values after update: [[4.946409 6.601863]]
Designated Priority: 1
Q-values before update: [[4.793282 6.033864]]
Q-values after update: [[4.7912154 6.019122 ]]
Designated Priority: 1
Q-values before update: [[4.472753  5.2667565]]
Q-values after update: [[4.4686127 5.2484436]]
Designated Priority: 1
Q-values before update: [[4.1134777 4.428728 ]]
Q-values after update: [[4.10863   4.4095263]]
Designated Priority: 1
Q-values before update: [[3.7068882 3.519968 ]]
Q-values after update: [[3.7127478 3.5097291]]
Designated Priority: 1
Q-values before update: [[3.853714  4.0215225]]
Q-values after update: [[3.8609738 4.0183454]]
Designated Priority: 1
Q-values before update: [[3.4190376 3.0649645]]
Q-values after update: [[3.4363725 3.0704358]]
Designated Priority: 1
Q-values before update: [[3.5315695 3.5195959]]
Q-values after update: [[3.5559301 3.534174 ]]
Designated Priority: 1
Q-values before update: [[3.6536274 3.989612 ]]
Q-values after update: [[3.6826165 4.0106397]]
Designated Priority: 1
Q-values before update: [[3.789507  4.4739757]]
Q-values after update: [[3.8114944 4.490164 ]]
Designated Priority: 1
Q-values before update: [[3.370243  3.5312002]]
Q-values after update: [[3.3961945 3.552013 ]]
Designated Priority: 1
Q-values before update: [[2.9205146 2.5323825]]
Q-values after update: [[2.9565063 2.5616875]]
Designated Priority: 1
Q-values before update: [[2.9632173 2.8942778]]
Q-values after update: [[3.0002978 2.9262934]]
Designated Priority: 3
Q-values before update: [[3.0092833 3.259782 ]]
Q-values after update: [[2.9827664 3.2299314]]
Episode 98 out of total 100, Total Reward: 17.0, Epsilon: 0.75, Current State: [ 0.12170377  0.17837828 -0.2130428  -0.544337  ], Steps Taken: 17
Designated Priority: 1
Q-values before update: [[4.768367  6.4364524]]
Q-values after update: [[4.766382 6.433417]]
Designated Priority: 1
Q-values before update: [[4.61919   6.4257894]]
Q-values after update: [[4.6197915 6.428732 ]]
Designated Priority: 1
Q-values before update: [[4.7627974 6.4334254]]
Q-values after update: [[4.7639217 6.438366 ]]
Designated Priority: 1
Q-values before update: [[4.6761746 6.0682573]]
Q-values after update: [[4.6740656 6.068025 ]]
Designated Priority: 1
Q-values before update: [[4.3771963 5.2802377]]
Q-values after update: [[4.373499 5.27879 ]]
Designated Priority: 1
Q-values before update: [[4.0132923 4.4285216]]
Q-values after update: [[4.0092387 4.426638 ]]
Designated Priority: 1
Q-values before update: [[3.6069238 3.5102198]]
Q-values after update: [[3.612942  3.5173554]]
Designated Priority: 1
Q-values before update: [[3.7196589 4.0010138]]
Q-values after update: [[3.725643  4.0094595]]
Designated Priority: 1
Q-values before update: [[3.2901795 3.0426936]]
Q-values after update: [[3.306053  3.0601852]]
Designated Priority: 1
Q-values before update: [[3.3696215 3.4815567]]
Q-values after update: [[3.3916953 3.5047863]]
Designated Priority: 1
Q-values before update: [[3.4613154 3.9347563]]
Q-values after update: [[3.4781528 3.953214 ]]
Designated Priority: 1
Q-values before update: [[3.0325952 2.9664257]]
Q-values after update: [[3.06025   2.9947932]]
Designated Priority: 1
Q-values before update: [[3.0852857 3.3635838]]
Q-values after update: [[3.107878  3.3879776]]
Designated Priority: 1
Q-values before update: [[2.6411364 2.3641   ]]
Q-values after update: [[2.6736233 2.397869 ]]
Designated Priority: 3
Q-values before update: [[2.6486003 2.6962113]]
Q-values after update: [[2.6212356 2.6274202]]
Episode 99 out of total 100, Total Reward: 15.0, Epsilon: 0.75, Current State: [ 0.13945703  0.58032525 -0.22367276 -1.2506613 ], Steps Taken: 15
Designated Priority: 1
Q-values before update: [[4.898426 6.568023]]
Q-values after update: [[4.895258  6.5508294]]
Designated Priority: 1
Q-values before update: [[4.888264  6.2839103]]
Q-values after update: [[4.879531  6.2554846]]
Designated Priority: 1
Q-values before update: [[4.5959883 5.4657626]]
Q-values after update: [[4.585713  5.4341645]]
Designated Priority: 1
Q-values before update: [[4.244727  4.5826344]]
Q-values after update: [[4.234954 4.550799]]
Designated Priority: 1
Q-values before update: [[3.8490553 3.6275985]]
Q-values after update: [[3.8489966 3.603735 ]]
Designated Priority: 1
Q-values before update: [[3.946013  4.1036177]]
Q-values after update: [[3.9476142 4.0882998]]
Designated Priority: 1
Q-values before update: [[3.5270963 3.1063564]]
Q-values after update: [[3.5379632 3.0988674]]
Designated Priority: 1
Q-values before update: [[3.5922565 3.5400424]]
Q-values after update: [[3.6036549 3.539809 ]]
Designated Priority: 1
Q-values before update: [[3.149487 2.524101]]
Q-values after update: [[3.1706946 2.5345812]]
Designated Priority: 1
Q-values before update: [[3.1766973 2.882569 ]]
Q-values after update: [[3.2009244 2.8963368]]
Designated Priority: 1
Q-values before update: [[3.207918  3.2734525]]
Q-values after update: [[3.228493  3.2877228]]
Designated Priority: 1
Q-values before update: [[2.770091  2.2412486]]
Q-values after update: [[2.8004649 2.2646863]]
Designated Priority: 3
Q-values before update: [[2.7536018 2.5538433]]
Q-values after update: [[2.720438  2.5169098]]
Episode 100 out of total 100, Total Reward: 13.0, Epsilon: 0.75, Current State: [ 0.10192543  0.21658376 -0.22546023 -0.69114405], Steps Taken: 13
[9.0, 9.0, 10.0, 10.0, 8.0, 10.0, 9.0, 10.0, 10.0, 10.0, 9.0, 13.0, 10.0, 8.0, 10.0, 8.0, 9.0, 9.0, 11.0, 10.0, 10.0, 10.0, 11.0, 12.0, 19.0, 27.0, 23.0, 23.0, 11.0, 11.0, 9.0, 8.0, 8.0, 11.0, 10.0, 13.0, 9.0, 12.0, 12.0, 12.0, 11.0, 10.0, 10.0, 12.0, 12.0, 10.0, 10.0, 12.0, 10.0, 11.0, 9.0, 11.0, 12.0, 10.0, 10.0, 20.0, 14.0, 11.0, 10.0, 9.0, 9.0, 10.0, 22.0, 32.0, 26.0, 43.0, 10.0, 14.0, 23.0, 22.0, 16.0, 21.0, 17.0, 17.0, 12.0, 19.0, 11.0, 14.0, 19.0, 17.0, 18.0, 19.0, 24.0, 12.0, 13.0, 15.0, 12.0, 10.0, 11.0, 14.0, 13.0, 17.0, 15.0, 24.0, 14.0, 13.0, 14.0, 17.0, 15.0, 13.0]
"""

episode_pattern = r'Episode (\d+) out of total \d+, Total Reward: ([\d.]+), Epsilon: [\d.]+, Current State: \[.*\], Steps Taken: (\d+)'

episodes = []
rewards = []
steps = []

matches = re.findall(episode_pattern, text)
for match in matches:
    episodes.append(int(match[0]))
    rewards.append(float(match[1]))
    steps.append(int(match[2]))
    print(f"Episode: {match[0]}, Reward: {match[1]}, Steps Taken: {match[2]}")

cumulative_steps = np.cumsum(steps)


window_size = 50
window = np.ones(window_size) / window_size
episode_return_smooth = np.convolve(rewards, window, mode='valid')

df = pd.DataFrame({

    'Episode': episodes[:len(episode_return_smooth)],  
    'Total_Reward': rewards[:len(episode_return_smooth)],  
    'Smoothed_Reward': episode_return_smooth,
    'Steps_Taken': steps[:len(episode_return_smooth)]
})

plt.figure(figsize=(12, 6))

plt.plot(df['Episode'], df['Smoothed_Reward'], color='blue', linewidth=1)

plt.xlabel('Episode')
plt.ylabel('Moving Average Reward over 50 steps')

plt.legend()
plt.show()

plt.figure(figsize=(12, 6))

plt.plot(cumulative_steps[:len(episode_return_smooth)], episode_return_smooth, linewidth=1)

plt.xlabel('Environment Step')
plt.ylabel('Moving Average Reward over 50 steps')

plt.legend()
plt.show()
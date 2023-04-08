from random import randint, choice

## General region codes
vncodes = choice([248,281,282,283,235,247,278,243,244,245,246,273,278,235,285,286,288,241,242,243,245,249,258,287,212,259,268,269,237,235,238,246,247,251,252,253,271,273,274,275,212,234,239,287,291,292,295,255,256,257,293,294,276,277,271,272,212,251,253,254,261,262,263,264,265,266,267,271,275,412,424,414,415,416,426])
mxcodes = choice([55,56,81,33,656,614,618,999,990,221,222,442,446,449,663,664,612,624,644,686,667,722,729,998,871,744,444,440,833,477,479,961,662,633,645,644,642,631,229,443,921,771,981,899,868])
svcodes = choice([70,71,72,73,74,75,76,77,78,79])
chcodes = choice([33,34,35,42,43,45,51,52,53,55,57,58,61,63,64,65,67,71,72,73,75])
E1 = choice([9,4.2,7])
E2 = choice([96])
E3 = choice([939,964])

## General range phone
us = "+1 "+"".join(str(randint(0, 9)) for _ in range(3))+"".join(str(randint(0, 9)) for _ in range(3))+"".join(str(randint(0, 9)) for _ in range(4))
colombia = "+57 "+f"3"+"".join(str(randint(0, 9)) for _ in range(9))
venezuela = "+58 "+f"{vncodes}"+"".join(str(randint(0, 9)) for _ in range(7))
mexico = "+52 "+f"{mxcodes}"+"".join(str(randint(0, 9)) for _ in range(7))
chile = "+56 "+f"{chcodes}"+"2"+"".join(str(randint(0, 9)) for _ in range(6))
elsalvador = "+503 "+f"{svcodes}"+"".join(str(randint(0, 9)) for _ in range(6))
guatemala = "+502 "+"".join(str(randint(0, 9)) for _ in range(8))
honduras = "+504 "+"".join(str(randint(0, 9)) for _ in range(8))
nicaragua = "+505 "+"".join(str(randint(0, 9)) for _ in range(8))

## Ecuador region codes
ecua1 = "+593 "+f"{E1}"+"".join(str(randint(0, 9)) for _ in range(8))
ecua2 = "+593 "+f"{E2}"+"".join(str(randint(0, 9)) for _ in range(7))
ecua3 = "+593 "+f"{E3}"+"".join(str(randint(0, 9)) for _ in range(6))
ecuador = choice([ecua1, ecua2, ecua3])

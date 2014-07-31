Deployment Order:

Deploy Relationship 
Deploy Auto Script 
Deploy Max Message Package



Further Information:

The response plan ranking was not correct for the INTERNAL WALLS / Internal Wall Vandalism / Serious or Offensive Vandalism (350 \ 350-120 \ 350-120-030 \ 350-120-030-010) classification.

Instead of applying the INTERNAL WALLS / Internal Wall Vandalism / Serious or Offensive Vandalism RP,  maximo  applied  INTERNAL WALLS / Internal Wall Vandalism because it was the same ranking of 65.

My code is slightly more logical, it chooses the most relevant, then the highest ranking RP. Maximo just chooses the highest ranked within the class structure, which isn’t optimal for our setup. 

Steps to resolve:

RP02550 – Change ranking to 70
RP00740 - Change ranking to 70
RP09110- Change ranking to  105
RP06460 - Change ranking to  35
RP06470 - Change ranking to  35

Matt is doing some unit testing now in dev, once this is signed off we will schedule a deployment to SIT.


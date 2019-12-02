#enter data from fangraphs.com for Tanner 

numpitches2013 = 756 #*season stats-more batted ball, the most number of pitches of each year*/
numpitches2014 = 2299
numpitches2015 = 1800

FBfract2013 = 0.626# /*fastball*/
FBfract2014 = 0.668 # /*frequences: game log-pitch type*/
FBfract2015 = 0.668

SLfract2013 = 0.200# /*slider*/
SLfract2014 = 0.146
SLfract2015 = 0.152

CBfract2013 = 0.098#  /*change-up*/
CBfract2014 = 0.084
CBfract2015 = 0.112

#CBfract2013 = 0.0#  /*change-up*/
#CBfract2014 = 0.0
#CBfract2015 = 0.0

#CHfract2013 = 0.0#  /*change-up*/
#CHfract2014 = 0.0
#CHfract2015 = 0.0

CHfract2013 = 0.077#  /*change-up*/
CHfract2014 = 0.102
CHfract2015 = 0.068

wFB2013 = 7.3 #  /*game log-pitch value*/
wFB2014 = 13.5
wFB2015 = -1.1

wSL2013 = 5.4
wSL2014 =  3.0
wSL2015 =  -3.4

#wCB2013 = 0.0
#wCB2014 = 0.0
#wCB2015 = 0.0

wCB2013 = 0.0
wCB2014 = 0.8
wCB2015 = -3.2

#wCH2013 = 0.0
#wCH2014 = 0.0  
#wCH2015 = 0.0

wCH2013 = 1.5
wCH2014 = 0.9  
wCH2015 = 1.0

# Compute quantities in Paine article

weightedpitches = numpitches2013 + 2*numpitches2014 + 3*numpitches2015
#weightedpitches =  10546    /* agrees with Paine */
print("The weighted pitches number is: ", weightedpitches)

weightednumFB = (FBfract2013*numpitches2013) + 2*(FBfract2014*numpitches2014) + 3*(FBfract2015*numpitches2015)
weightedFBfract = weightednumFB/weightedpitches
#weightedFBfract =  0.75632  /* agrees with Paine */
print("The weighted weighted FBfract is: ", weightedFBfract)

weightednumSL = (SLfract2013*numpitches2013) + 2*(SLfract2014*numpitches2014) + 3*(SLfract2015*numpitches2015)
weightedSLfract = weightednumSL/weightedpitches 
#weightedSLfract =  0.24339  /* agrees with Paine */ 
print("The weighted weighted SLfract is: ", weightedSLfract)

weightednumCB = (CBfract2013*numpitches2013) + 2*(CBfract2014*numpitches2014) + 3*(CBfract2015*numpitches2015)
weightedCBfract = weightednumCB/weightedpitches; 
print("The weighted weighted CBfract is: ", weightedCBfract)

weightednumCH = (CHfract2013*numpitches2013) + 2*(CHfract2014*numpitches2014) + 3*(CHfract2015*numpitches2015)
weightedCHfract = weightednumCH/weightedpitches; 
print("The weighted weighted CHfract is: ", weightedCHfract)

Totalvalue2013 = wFB2013 + wSL2013 + wCB2013 + wCH2013
Totalvalue2014 = wFB2014 + wSL2014 + wCB2014 + wCH2014
Totalvalue2015 = wFB2015 + wSL2015 + wCB2015 + wCH2015
weightedTotalvalue = Totalvalue2013 + 2*Totalvalue2014 + 3*Totalvalue2015
overallvalue = 100*weightedTotalvalue/weightedpitches
#overallvalue = -0.61066   /* agrees with Paine */
print("The overallvalue is: ", overallvalue)

weightedwFB = wFB2013 + 2*wFB2014 + 3*wFB2015
weightedwSL = wSL2013 + 2*wSL2014 + 3*wSL2015
weightedwCB = wCB2013 + 2*wCB2014 + 3*wCB2015
weightedwCH = wCH2013 + 2*wCH2014 + 3*wCH2015


weightedwFBper100 = 100*weightedwFB/weightednumFB
weightedwSLper100 = 100*weightedwSL/weightednumSL
weightedwCBper100 = 100*weightedwCB/weightednumCB
weightedwCHper100 = 100*weightedwCH/weightednumCH

print(weightedwFBper100, weightedwSLper100, weightedwCBper100, weightedwCHper100)

relvalueFB = weightedwFBper100 - weightedwSLper100 #-  weightedwCBper100 - weightedwCHper100  #don't consider CH because too few pitches */
#relvalueFB = -2.5039   /* agrees with Paine */
print("The relvalueFB is: ", relvalueFB)

relvalueSL = weightedwSLper100 - weightedwFBper100 #-  weightedwCBper100 - weightedwCHper100   # don't consider CH because too few pitches */
#relvalueSL =  2.5039   /* agrees with Paine */
print("The relvalueSL is: ", relvalueSL)

relvalueCB = weightedwCBper100 - weightedwFBper100 #-  weightedwSLper100 - weightedwCHper100  # don't consider CH because too few pitches */
#relvalueSL =  2.5039   /* agrees with Paine */
print("The relvalueCB is: ", relvalueCB)

relvalueCH = weightedwCHper100 - weightedwFBper100 #-  weightedwCBper100 - weightedwSLper100  # don't consider CH because too few pitches */
#relvalueSL =  2.5039   /* agrees with Paine */
print("The relvaluCH is: ", relvalueCH)

Nashscore = (weightedFBfract*relvalueFB*relvalueFB + weightedSLfract*relvalueSL*relvalueSL + weightedCBfract*relvalueCB*relvalueCB + weightedCHfract*relvalueCH*relvalueCH)**0.5
#Nashscore =  2.5035    /* almost agrees with Paine */
print("The Nashscore is: ", Nashscore)










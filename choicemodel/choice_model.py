import numpy as np
import pandas as pd

# Bring in the households by segment and block group data
# Read it from Excel as a Pandas DataFrame
# Transpose it to make it so that market segments are rows and blocks are columns

TNDatadf = pd.DataFrame.transpose(pd.read_excel(r'/home/MattBingham/TNdata.xlsx'))

# print (TNDatadf)

# Convert the Pandas DataFrame to a NumPy Array
# Hmm I know how to just grab a column - see below - but not all but 1st row 1st column
# Do all of above except with unlabled data

TNData = pd.DataFrame.transpose(pd.read_excel(r'/home/MattBingham/TNdataNoLabels.xlsx'))

TNDatana = TNData.values[:, :]

# print(TNDatana)

# Get participation coefficients as DataFrame

PartCoeffdf = pd.read_excel(r'/home/MattBingham/PartCoeff.xlsx')

# print(PartCoeffdf)

PartCoeffLabels = PartCoeffdf.values[:, [0]]

# print(PartLabels)

# Drop the label and turn to NumPy Array

PartCoeffna = PartCoeffdf.values[:, [1]].astype(float)

# print(PartCoeffna)

# Base (not interacted) conditional logit level
# Plan 1 is P1

P1On = np.array([1])
P1PeakRate = np.array([.34])
P1OffPeakRate = np.array([.08])
P1PeakIs2to5 = np.array([0])
P1PeakIs2to6 = np.array([1])
P1PeakIs2to8 = np.array([0])
P1PeakIs3to6 = np.array([0])
P1PeakIs4to7 = np.array([0])
P1PeakIs5to7 = np.array([0])
P1PeakIsSummer = np.array([1])
P1PeakIsSumWint = np.array([0])

# Plan 2 is P2
P2On = np.array([1])
P2PeakRate = np.array([.27])
P2OffPeakRate = np.array([.09])
P2PeakIs2to5 = np.array([0])
P2PeakIs2to6 = np.array([0])
P2PeakIs2to8 = np.array([1])
P2PeakIs3to6 = np.array([0])
P2PeakIs4to7 = np.array([0])
P2PeakIs5to7 = np.array([0])
P2PeakIsSummer = np.array([0])
P2PeakIsSumWint = np.array([1])

# Base Coefficients
PeakRateCoeff = np.array([-8.76])
OffPeakRateCoeff = np.array([-1.5064])
PeakIs2to5Coeff = np.array([.2482])
PeakIs2to6Coeff = np.array([.3314])
PeakIs2to8Coeff = np.array([0])
PeakIs3to6Coeff = np.array([.2726])
PeakIs4to7Coeff = np.array([.1905])
PeakIs5to7Coeff = np.array([.2247])
SummerCoeff = np.array([-.2002])
SummerAndWinterCoefficient = np.array([0])

# Plan 1 and 2 Exponentiated Utility
P1XU = P1On * np.exp(
    PeakRateCoeff * P1PeakRate + OffPeakRateCoeff * P1OffPeakRate + PeakIs2to5Coeff * P1PeakIs2to5 + PeakIs2to6Coeff * P1PeakIs2to6 + PeakIs2to8Coeff * P1PeakIs2to8 + PeakIs3to6Coeff * P1PeakIs3to6 + PeakIs4to7Coeff * P1PeakIs4to7 + PeakIs5to7Coeff * P1PeakIs5to7 + SummerCoeff * P1PeakIsSummer +
    SummerAndWinterCoefficient * P1PeakIsSumWint)
P2XU = P2On * np.exp(
    PeakRateCoeff * P2PeakRate + OffPeakRateCoeff * P2OffPeakRate + PeakIs2to5Coeff * P2PeakIs2to5 + PeakIs2to6Coeff * P2PeakIs2to6 + PeakIs2to8Coeff * P2PeakIs2to8 + PeakIs3to6Coeff * P2PeakIs3to6 + PeakIs4to7Coeff * P2PeakIs4to7 + PeakIs5to7Coeff * P2PeakIs5to7 + SummerCoeff * P2PeakIsSummer +
    SummerAndWinterCoefficient * P2PeakIsSumWint)
SumXU = (P1XU + P2XU)
ProbP1 = P1XU / SumXU
ProbP2 = P2XU / SumXU
ScaleFactor = np.array([.3126567])
ExScaleLogSum = np.exp(ScaleFactor * np.log(SumXU))
PartRate = ExScaleLogSum / (ExScaleLogSum + np.exp(-1 * PartCoeffna))

# print(PartRate)
# Calculate Plan Rates by Segment
P1RatesBySeg = np.multiply(ProbP1, PartRate)
P2RatesBySeg = np.multiply(ProbP2, PartRate)
# Give them some titles
P1RatesBySegCols = ["Plan 1 Rate"]
P2RatesBySegCols = ["Plan 2 Rate"]
LP1RateBySeg = pd.DataFrame(P1RatesBySeg, index=PartCoeffLabels, columns=P1RatesBySegCols)
LP2RateBySeg = pd.DataFrame(P2RatesBySeg, index=PartCoeffLabels, columns=P2RatesBySegCols)

print(LP1RateBySeg)

print(LP2RateBySeg)

# Calculate Plan Numbers by Segment
P1NumBySegBlock = np.multiply(P1RatesBySeg, TNDatana)

P2NumBySegBlock = np.multiply(P2RatesBySeg, TNDatana)

# Sum over blocks to get the regional total - the "axis = 1" bit goes over columns 0 is over rows

P1NumBySeg = P1NumBySegBlock.sum(axis=1)

P2NumBySeg = P2NumBySegBlock.sum(axis=1)

# Give them some titles
P1NumBySegCols = ["Plan 1 Number"]

P2NumBySegCols = ["Plan 2 Number"]

LP1NumBySeg = pd.DataFrame(P1NumBySeg, index=PartCoeffLabels, columns=P1NumBySegCols)

LP2NumBySeg = pd.DataFrame(P2NumBySeg, index=PartCoeffLabels, columns=P2NumBySegCols)

print(LP1NumBySeg)
print(LP2NumBySeg)

df = pd.DataFrame(P1RatesBySeg, index=PartCoeffLabels)

# print(df)

# df.to_csv('df.csv', index=True, header=True, sep=' ')

# print(P2RatesBySeg)

# Use append to put these results next to each other, (concat puts them on the end)

# Getting error "only integer scalar arrays can be converted to a scalar index" try again later

# P12NumBySeg = np.concatenate([P1NumBySeg,P2NumBySeg])

# print(P12NumBySeg)

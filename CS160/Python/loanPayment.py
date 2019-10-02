import math;

presentValue = int(input("Present Value: "));
ratePerPeriod = float(input("Rate Per Period: ")) * 0.001;
numberOfPeriods = int(input("Number Of Periods: "));

topLine = pow((1+ratePerPeriod), numberOfPeriods) - 1;
bottomLine = ratePerPeriod * pow((1 + ratePerPeriod), numberOfPeriods);
value = topLine/bottomLine;
print presentValue/value

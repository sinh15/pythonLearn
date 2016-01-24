# Assignment 6.5 (first week course2)
text = "X-DSPAM-Confidence:    0.8475";

length = len(text)
fSpace = text.find(' ')
number = float(text[fSpace:length].strip())

print number
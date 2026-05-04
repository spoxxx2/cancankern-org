import math
FINAL=1704.96
TARGET=1700.00
STABILITY=1-(abs(FINAL-TARGET)/TARGET)
def f(m=3):
 b=88.0+(STABILITY*10)
 c=math.log(m+1)*2.5
 p=min(99.9,b+c)
 print(f'--- OMNI PURITY: {p:.2f}% ---')
if __name__=='__main__': f()

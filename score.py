#score_file = open("score.txt","w",encoding="utf8")
#print("수학:0",file=score_file)
#print("영어:50",file=score_file)
#score_file.close()
#score_file.write("\n체육:60")
#score_file.write("\n사회:80")
score_file =open("score.txt","r",encoding="utf8")
#print(score_file.readline(),end="")
#print(score_file.readline(),end="")
#while True:
    #line= score_file.readline()
    #if not line:
        #break
    #print(line,end="")
lines =score_file.readlines()
for line in lines:
    print(line,end="")
score_file.close()
# tk001
Tkinter라이브러리를 활용한예제
# create a new repository on the command line
echo "# tk001" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jnnaver/tk001.git
git push -u origin main


### fatal: refusing to merge unrelated histories 오류는
 로컬 브랜치와 원격 브랜치의 커밋 히스토리가 서로 다를 때 발생합니다. 주로 다음과 같은 상황에서 발생합니다:

로컬에서 새로운 저장소를 초기화했지만, 원격 저장소에 이미 커밋이 존재하는 경우.
원격 저장소에서 변경 사항이 생겼지만, 로컬에서 그 변경 사항을 가져오지 않은 경우.
--allow-unrelated-histories 옵션을 사용하여 병합할 수 있습니다.

git fetch origin
허용된 히스토리 병합 사용하기:

git merge origin/main --allow-unrelated-histories
여기서 main은 원격 브랜치의 이름입니다.

변경 사항 푸시하기 (필요한 경우):
병합이 완료되면 원격 저장소에 푸시합니다:

git push origin main
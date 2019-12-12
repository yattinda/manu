import random
from Modan import elements
#change from



for quiznum in range(1):
    #クイズと答えのファイル作成、枚数はrange()
    quiz_file = open("./quiz/quiz{}.txt".format(quiznum +1),"w")
    answer_file = open("./answer/answer{}txt".format(quiznum +1),"w")

    quiz_file.write("\n\n")

    #正しい答えをシャッフル
    elements_key = list(elements.keys())
    random.shuffle(elements_key)
    #print(elements_key)
    #問題作成
for QUIZnum in range(len(elements_key)):
    correct_answer = elements[elements_key[QUIZnum]]

    #print("correct_answer:" ,correct_answer)
    wrong_answer = list(elements.values())
    #wrong_answerからcorrect_answer
    #print(wrong_answer)
    del wrong_answer[wrong_answer.index(correct_answer)]
    #無作為抽出
    wrong_answer = random.sample(wrong_answer,3)
    #print(wrong_answer)
    #選択肢作成
    answer_options = wrong_answer + [correct_answer]
    print("answer_op:"  ,answer_options)
    random.shuffle(answer_options)

    #問題文
    quiz_file.write("{}.{}\n\n".format(QUIZnum +1 ,elements_key[QUIZnum]))
    #選択肢、range()は択数、変更時はline26のsample変更
    for i in range(4):
        quiz_file.write("{} {}\n".format("①②③④"[i],answer_options[i]))

    quiz_file.write("\n")

    #答え
    print("DEBUG", answer_options.index(correct_answer))
    answer_file.write("{}.{}\n".format(QUIZnum +1 , "①②③④"[answer_options.index(correct_answer)]))


quiz_file.close
answer_file.close

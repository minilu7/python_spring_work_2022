



algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
id = [1,2,3,4,5,6,7,8,9,10]
zip (id, algoritm)
import csv
with open("algoritm.csv", "w") as f:
  writer = csv.writer(f, delimiter='\t')
  writer.writerows(zip(id, algoritm))
quit()


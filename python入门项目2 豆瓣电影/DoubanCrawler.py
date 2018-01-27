import expanddouban
from bs4 import BeautifulSoup
import csv
import codecs

def Movie_url(Lei_xing,Di_qu):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    Xu_qiu_url = url + "," + Lei_xing + "," +Di_qu
    return Xu_qiu_url

class Movie(object):
    def __init__(self,name,Ping_fen,Lei_xing,Di_qu,Ye_mian_link,Hai_bao_link):
        self.name = name
        self.Ping_fen = Ping_fen
        self.Lei_xing = Lei_xing
        self.Di_qu = Di_qu
        self.Ye_mian_link = Ye_mian_link
        self.Hai_bao_link = Hai_bao_link
    def __str__(self):
        return (self.name, self.Ping_fen, self.Lei_xing, self.Di_qu, self.Ye_mian_link, self.Hai_bao_link)

def Html(di_qu,lei_xing):
    html = expanddouban.getHtml(Movie_url(di_qu, lei_xing), loadmore=True)
    soup = BeautifulSoup(html, "lxml")
    return soup.find(id="content").find(class_="list-wp").find_all("a", recursive=False)

def Get_movies(Di_qu,Lei_xing):
    movies = []
    for temp_di_qu in Di_qu:
        Xin_xi = Html(temp_di_qu,Lei_xing)

        for temp in Xin_xi:
            movie_name = str(temp.find(class_="title"))[39:-7]
            movie_ping_fen = str(temp.find(class_="rate"))[38:-7]
            movie_lei_xing = Lei_xing
            movie_di_qu = temp_di_qu
            movie_ye_mian = temp.get("href")
            movie_hai_bao = temp.find("img").get("src")
            movies.append(Movie(movie_name,movie_ping_fen,movie_di_qu,movie_lei_xing,movie_ye_mian,movie_hai_bao).__str__())

    return movies

Di_qu = ["大陆","美国","香港","台湾","日本","韩国","英国","法国","德国","意大利","西班牙","印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]

Lei_xing = ["情色","暴力","恐怖"]
Moive_mu_lu = []
for temp_lei_xing in Lei_xing:
    movies = Get_movies(Di_qu,temp_lei_xing)
    Moive_mu_lu += movies

with open("movies.csv","w", encoding='utf-8') as csvfile:
    movies_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    movies_writer.writerow(["电影名", "评分", "地区","类型","电影链接","海报链接"])
    movies_writer.writerows(Moive_mu_lu)

Qing_se = []
Bao_li = []
Kong_bu = []
for temp in Moive_mu_lu:
    if temp[3] == "情色":
        Qing_se.append(temp)
    elif temp[3] == "暴力":
        Bao_li.append(temp)
    elif temp[3] == "恐怖":
        Kong_bu.append(temp)


Qing_se_num = len(Qing_se)
Bao_li_num = len(Bao_li)
Kong_bu_num = len(Kong_bu)

def Pai_ming(lei_xing):
    Di_qu_dict = {"大陆":0,"美国":0,"香港":0,"台湾":0,"日本":0,"韩国":0,"英国":0,"法国":0,"德国":0,"意大利":0,"西班牙":0,"印度":0,"泰国":0,"俄罗斯":0,"伊朗":0,"加拿大":0,"澳大利亚":0,"爱尔兰":0,"瑞典":0,"巴西":0,"丹麦":0}
    for temp in lei_xing:
        Di_qu_dict[temp[2]] += 1
    Di_qu_dict = sorted(Di_qu_dict.items(),key=lambda x:x[1],reverse=True)
    return Di_qu_dict

Qing_pai = Pai_ming(Qing_se)
Bao_pai = Pai_ming(Bao_li)
Kong_pai = Pai_ming(Kong_bu)

Qing_pai_1 = (Qing_pai[0])[0]
Qing_1_bai_fen = (Qing_pai[0])[1]/len(Qing_se)
Qing_1_bai_fen = round(Qing_1_bai_fen,4)*100

Qing_pai_2 = (Qing_pai[1])[0]
Qing_2_bai_fen = (Qing_pai[1])[1]/len(Qing_se)
Qing_2_bai_fen = round(Qing_2_bai_fen,4)*100

Qing_pai_3 = (Qing_pai[2])[0]
Qing_3_bai_fen = (Qing_pai[2])[1]/len(Qing_se)
Qing_3_bai_fen = round(Qing_3_bai_fen,4)*100


Bao_pai_1 = (Bao_pai[0])[0]
Bao_1_bai_fen = (Bao_pai[0])[1]/len(Bao_li)
Bao_1_bai_fen = round(Bao_1_bai_fen,4)*100

Bao_pai_2 = (Bao_pai[1])[0]
Bao_2_bai_fen = (Bao_pai[1])[1]/len(Bao_li)
Bao_2_bai_fen = round(Bao_2_bai_fen,4)*100

Bao_pai_3 = (Bao_pai[2])[0]
Bao_3_bai_fen = (Bao_pai[2])[1]/len(Bao_li)
Bao_3_bai_fen = round(Bao_3_bai_fen,4)*100


Kong_pai_1 = (Kong_pai[0])[0]
Kong_1_bai_fen = (Kong_pai[0])[1]/len(Kong_bu)
Kong_1_bai_fen = round(Kong_1_bai_fen,4)*100

Kong_pai_2 = (Kong_pai[1])[0]
Kong_2_bai_fen = (Kong_pai[1])[1]/len(Kong_bu)
Kong_2_bai_fen = round(Kong_2_bai_fen,4)*100

Kong_pai_3 = (Kong_pai[2])[0]
Kong_3_bai_fen = (Kong_pai[2])[1]/len(Kong_bu)
Kong_3_bai_fen = round(Kong_3_bai_fen,4)*100

f = codecs.open("output.txt","w","utf-8")

f.write("情色类别电影数量排名第一的是{},百分比是{}%\n".format(Qing_pai_1,Qing_1_bai_fen))
f.write("情色类别电影数量排名第二的是{},百分比是{}%\n".format(Qing_pai_2,Qing_2_bai_fen))
f.write("情色类别电影数量排名第三的是{},百分比是{}%\n".format(Qing_pai_3,Qing_3_bai_fen))

f.write("暴力类别电影数量排名第一的是{},百分比是{}%\n".format(Bao_pai_1,Bao_1_bai_fen))
f.write("暴力类别电影数量排名第二的是{},百分比是{}%\n".format(Bao_pai_2,Bao_2_bai_fen))
f.write("暴力类别电影数量排名第三的是{},百分比是{}%\n".format(Bao_pai_3,Bao_3_bai_fen))

f.write("恐怖类别电影数量排名第一的是{},百分比是{}%\n".format(Kong_pai_1,Kong_1_bai_fen))
f.write("恐怖类别电影数量排名第二的是{},百分比是{}%\n".format(Kong_pai_2,Kong_2_bai_fen))
f.write("恐怖类别电影数量排名第三的是{},百分比是{}%\n".format(Kong_pai_3,Kong_3_bai_fen))

f.close()
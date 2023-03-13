from bs4 import BeautifulSoup
import requests
import openpyxl

# reading the xlsx file
wb = openpyxl.load_workbook("/home/sathvick/Downloads/Input.xlsx")
ws=wb['Sheet1']
rows = ws.iter_rows(min_row=2,max_row=115,min_col=1,max_col=2)

# unpacking row tuple
for a,b in rows:
    url=b.value

# to make it look like a request from browser 
    headers= { 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}
    source = requests.get(url,headers=headers).text

    soup= BeautifulSoup(source,'lxml')
    # print(soup.prettify())

    url_name=url.split('/')[3]
# creating new file
    file=open("/home/sathvick/python/Extras/%s.txt"%(url_name),"w")  
    
    # csv_file= open('%s.csv'%(url_name),'w')
    # csv_writer=csv.writer(csv_file)
    # csv_writer.writerow()
    try:
        article=soup.find('article')
        headline=article.h1.text

        str_headline=str(headline)
        file.write(str_headline)
        # csv_writer.writerow(str_headline)
        divtag= article.find('div',class_='td-post-content')
        for summary in divtag.find_all('p'):
            # print(summary.text)
            # print()
            soup_summary=str(summary.text)
            file.write(soup_summary)
        #     csv_writer.writerow(soup_summary)
        # csv_file.close()
        file.flush()
        file.close()
    
    except Exception as e:
        headline= None

# article=soup.find('article')
# headline=article.h1.text
# print(headline)
# summary_headline=article.find('div',class_='td-post-content').p.text
# print(summary_headline)
# summary=article.find('div',class_='td-post-content').p.text
# print(summary)


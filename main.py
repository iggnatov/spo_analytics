import requests
import csv

if __name__ == '__main__':

    j = requests.get(
        "https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&professional_role=96&area=1&experience=noExperience&page=0&per_page=100")
    d = j.json()
    d_pages = int(d['pages'])
    cnt = 0
    cnt_pages = 0

    with open("output.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(["counter", "general_id", "item_name", "requirement"])

        for i in range(d_pages):
            print(i)
            j = requests.get(
                f"https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&professional_role=96&area=1&experience=noExperience&page={i}&per_page=100")
            # print(j)
            d = j.json()
            # d_pages = int(d['pages'])
            cnt_pages += 1

            for counter, item in enumerate(d['items']):
                print(f"{counter} general_id: {item['id']}, item_name: {item['name']}, item_city: {item['area']['name']}, "
                      f"item_sinppets: {item['snippet']['requirement']}")
                file_writer.writerow([counter, item['id'], item['name'], item['snippet']['requirement']])
                cnt += 1

    print(cnt)
    print(cnt_pages)
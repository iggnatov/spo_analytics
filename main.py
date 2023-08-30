import requests
import csv


class RequestLink:
    # https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies
    text = "text=" + "%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82"
    professional_role = "&professional_role=" + str(96)
    area = "&area=" + str(1)
    experience = "&experience=" + "noExperience"
    page = "&page" + str(0)
    per_page = "&per_page=" + str(100)
    link = "https://api.hh.ru/vacancies?"


if __name__ == '__main__':

    j = requests.get(
        "https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&professional_role=96&area=1&page=0&per_page=100")
    d = j.json()
    d_pages = int(d['pages'])
    print(d_pages)
    cnt = 0
    cnt_pages = 0

    with open("output.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(["general_id", "item_name", "requirement", "responsibility", "experience", "salary"])

        for i in range(d_pages):
            print(i, end=' ')
            j = requests.get(
                f"https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&professional_role=96&area=1&page={i}&per_page=100")

            d = j.json()
            # d_pages = int(d['pages'])
            cnt_pages += 1
            print(len(d['items']))

            for counter, item in enumerate(d['items']):
                # salary
                salary = ''
                salary_from = ''
                salary_to = ''
                if item['salary'] is not None:
                    for el in item['salary']:
                        if item['salary']['from'] is not None:
                            salary_from = str(item['salary']['from'])
                        if item['salary']['to'] is not None:
                            str(item['salary']['to'])

                        salary = salary_from + ',' + salary_to

                # key_skills
                # key_skills = ''
                # try:
                #     if item['salary'] is not None:
                #         for counter2, el in item['key_skills']:
                #             key_skills += el + ','
                # except KeyError:
                #     pass

                file_writer.writerow([item["id"],
                                      item["name"],
                                      item["snippet"]["requirement"],
                                      item["snippet"]["responsibility"],
                                      item["experience"]["name"],
                                      salary
                                      ])
                cnt += 1
                # if cnt < 10:
                #     print(item)

    print('\n')
    print('cnt_pages: ', cnt_pages)
    print('cnt: ', cnt)

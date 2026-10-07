# Selected original functions; file IO and full script omitted.


def get_page_xpath(page_number):
    if page_number <= 10:
        return f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{page_number}]/a"
    elif (page_number - 1) % 10 == 0:  # 10, 20 gibi "Next Page" düğmesi
        if page_number == 11:
            return "/html/body/div/div[2]/div[2]/div[2]/ul/li[11]/a"  # 10'dan 11'e geçiş
        else:
            return "/html/body/div/div[2]/div[2]/div[2]/ul/li[12]/a"  # 20'den 21 geçiş
    else:
        inner_page_number = (page_number - 1) % 10 + 2
        return f"/html/body/div/div[2]/div[2]/div[2]/ul/li[{inner_page_number}]/a"

import requests
import pdb

cookies = {
    'JSESSIONID': 'BDDE003DE0698585943E21EF978B3AC2',
    'cfid': 'a5e807f6-bb6f-4664-a1ad-dac689f3c9e1',
    'cftoken': '0',
    'AWSALB': 'OYUqY2rKyXpHVaQHO/5Zdz5w6B3+jMOFfTOGmSzF42LwPwKzR4XrydIhhD0i6LOKPvgYRxjm/QHiOl/QuaSeqIVx8I6vuJDErfJc3J8jVElh3aO6LRIHAgXlG98L',
    'AWSALBCORS': 'OYUqY2rKyXpHVaQHO/5Zdz5w6B3+jMOFfTOGmSzF42LwPwKzR4XrydIhhD0i6LOKPvgYRxjm/QHiOl/QuaSeqIVx8I6vuJDErfJc3J8jVElh3aO6LRIHAgXlG98L',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'JSESSIONID=BDDE003DE0698585943E21EF978B3AC2; cfid=a5e807f6-bb6f-4664-a1ad-dac689f3c9e1; cftoken=0; AWSALB=OYUqY2rKyXpHVaQHO/5Zdz5w6B3+jMOFfTOGmSzF42LwPwKzR4XrydIhhD0i6LOKPvgYRxjm/QHiOl/QuaSeqIVx8I6vuJDErfJc3J8jVElh3aO6LRIHAgXlG98L; AWSALBCORS=OYUqY2rKyXpHVaQHO/5Zdz5w6B3+jMOFfTOGmSzF42LwPwKzR4XrydIhhD0i6LOKPvgYRxjm/QHiOl/QuaSeqIVx8I6vuJDErfJc3J8jVElh3aO6LRIHAgXlG98L',
    'origin': 'https://garrett.marylandtaxsale.com',
    'priority': 'u=0, i',
    'referer': 'https://garrett.marylandtaxsale.com/index.cfm?folder=auctionResults&mode=preview',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'folder': 'auctionResults',
    'mode': 'preview',
}
response = requests.get('https://garrett.marylandtaxsale.com/index.cfm', params=params, cookies=cookies, headers=headers)
pdb.set_trace()
import asyncio
from aio_easycodefpy import Codef, ServiceType

demo_client_id = ''
demo_client_secret = ''

client_id = ''
client_secret = ''

public_key = ''

async def main():
    # 비동기 컨텍스트 매니저 사용 가능
    async with Codef() as codef:
        codef.public_key = public_key

        # 데모 클라이언트 정보 설정
        # - 데모 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
        # - 데모 서비스로 상품 조회 요청시 필수 입력 항목
        codef.set_demo_client_info(demo_client_id, demo_client_secret)

        # 정식 클라이언트 정보 설정
        # - 정식 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
        # - 정식 서비스로 상품 조회 요청시 필수 입력 항목
        codef.set_client_info(client_id, client_secret)


        # 요청 파라미터 설정
        # - 각 상품별 파라미터를 설정(https://developer.codef.io/products)
        parameter = {
            'connectedId': '8PQI4dQ......hKLhTnZ',
            'organization': '0004',
        }

        # 코드에프 정보 조회 요청
        # - 서비스타입(0:정식, 1:데모, 2:샌드박스)
        # 개인 보유계좌 조회 (https://developer.codef.io/products/bank/common/p/account)
        product_url = "/v1/kr/bank/p/account/account-list"
        res = await codef.request_product(product_url, ServiceType.SANDBOX, parameter)
        print(res)


asyncio.get_event_loop().run_until_complete(main())
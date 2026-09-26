from blockchain import HashChain

# 아래의 if문을 통해 해당 파일에서 코드를 실행할 떄만 아래 실행 결과가 출력되도록 설정
if __name__ == "__main__":
    blockchain = HashChain()
    blockchain.add_block("Alice -> Bob : 10 BTC")
    blockchain.add_block("Bob -> Carol : 5 BTC")
    blockchain.add_block("Carol -> Dabe : 2 BTC")

    print("=== 체인 상태 ===")
    for block in blockchain.chain:
        print(block)

    # 정상 상태에서의 검증
    print("체인 검증 결과: ", blockchain.is_valid())

    print("\n=== 블록 1의 데이터를 몰래 변조 시도 ===")
    blockchain.chain[2].data = "Alice -> Bob : 1000 BTC"
    # 변조 후 검증
    print("체인 검증 결과: ", blockchain.is_valid())

    """
    __name__ : 파이썬이 모든 파일에 자동을 부여하는 값
    - 그 파일을 직접 실행하면 __main__이 됨
    - 다른 파일에서 import되면 파일 이름인 "main"이 됨
    - if __name__ == "__main__":은 이 값을 확인해서 이 파일이 직접 실행될 때만 아래 코드를 돌리라는 뜻의 조건문
    - 지금 코드에서는 python main.py로 직접 돌릴 떄만 블록체인 테스트를 실행하게 해주는 안전장치
    - 추후 다른 파일이 이 파일을 import할 때, 이 테스트 코드가 멋대로 같이 실행되는 걸 막아주는 역할
    """
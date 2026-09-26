from block import Block

class HashChain:
    def __init__(self):
        # 체인이 생성되자마자 제네시스 블록 하나를 자동으로 만들어서 리스트에 넣어둠
        # 즉, HashChain 객체는 항상 최소 1개의 블록(제네시스)을 갖고 시작함
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # 체인의 첫 블록 (이전 해시가 없으니 "0"으로 채움)
        # 모든 블록은 "이전 블록의 해시"를 가져야 하는데, 첫 블록은 가리킬 대상이 없으므로 
        # previous_hash 자리를 임의의 고정값 "0"어로 채워서 체인을 시작함
        return Block(0, "Genisis Block", "0")

    def get_latest_block(self):
        # 체인에서 가장 마지막(가장 최근에 추가된) 블록을 반환
        # 새 블록을 추가할 때 "직전 블록"이 필요하므로 이 함수를 사용
        return self.chain[-1]

    def add_block(self, data):
        # 1. 현재 체인의 마지막 블록을 가져옴 (새 블록이 이어붙을 대상)
        latest = self.get_latest_block()

        # 2. 새 블록을 생성하면서, latest.hash(직전 블록이 이미 계산해둔 해시값)를 새 블록의 previous_hash로 그래돌 넘겨줌
        # > 이 한 줄이 바로 블록끼리 사슬처럼 연결되는 과정임
        new_block = Block(len(self.chain), data, latest.hash)

        # 3. 완성된 블록을 체인 리스트 끝에 추가
        self.chain.append(new_block)

    def is_valid(self):
        # 제네시스 블록은 비교 대상이 없으므로 검증에서 제외한 후 인덱스 1번 블록부터 끝까지 순서대로 검증함
        for i in range(1, len(self.chain)):
            current = self.chain[i] # 지금 검사하는 블록
            previous = self.chain[i-1] # 바로 앞 블록

            if current.hash != current.calculate_hash():
                # 1. 저장된 해시 vs 재계산한 해시 불일치 -> data가 변조됨
                print(f"블록 {current.index}: 데이터가 변조됨 (해시 불일치)")
                return False

            if current.previous_hash != previous.hash:
                # 2. current 블록에 저장된 previous_hash값 vs previous 블록의 실제 hash 값 불일치 -> 연결이 조작됨
                print(f"블록 {current.index}: 체인 연결이 끊김")
                return False

        return True
from block import Block

class HashChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # 체인의 첫 블록 (이전 해시가 없으니 "0"으로 채움)
        return Block(0, "Genisis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest = self.get_latest_block()
        new_block = Block(len(self.chain), data, latest.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calcuate_hash():
                print(f"블록 {current.index}: 데이터가 변조됨 (해시 불일치)")
                return False

            if current.previous_hash != previous.hash:
                print(f"블록 {current.index}: 체인 연결이 끊김")
                return False

        return True
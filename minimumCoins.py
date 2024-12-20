class SinglyLinkedListNode:
    def __init__(self, coins):
        self.coins = coins
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
               

    def insertNode(self, coins):
        nodeData = SinglyLinkedListNode(coins)

        if not self.head:
            self.head = nodeData
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nodeData

def getMinimumCoins(avilableCoins, totalSum):
    result = []
    remaingSum = totalSum
    for coin in avilableCoins:
        while remaingSum >= coin:
            result.append(coin)
            remaingSum -= coin

    return result

if __name__ == '__main__':
    totalSum = int(input("Enter the total sum:"))
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    linkedList = SinglyLinkedList()
    for coin in coins:
        linkedList.insertNode(coin)

    print(f"\nFor the total sum {totalSum}:")
    min_coins = getMinimumCoins(coins, totalSum)
        
    if isinstance(min_coins, list):
        print(f"The minimum coins needed to make the sum {totalSum} are: {min_coins}")
    else:
        print(min_coins)
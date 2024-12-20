class SLLNode:
    def __init__(self, nodeData):
        self.data = nodeData
        self.next = None  

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertNode(self, nodeData):
        node = SLLNode(nodeData)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def countCoins(self):
        coin_count = {}
        current = self.head
        while current:
            if current.data in coin_count:
                coin_count[current.data] += 1
            else:
                coin_count[current.data] = 1
            current = current.next
        
        return coin_count


def atm(linkedList, totalSumForPaying, userSum):
    rest = userSum - totalSumForPaying
    if rest == 0:
        return "Thank you for paying!"
    elif rest < 0:
        return "User has not given enough money."
    else:
        coins = [10, 5, 2, 1]  
        coin_count = linkedList.countCoins()  
        result = []

        for coin in coins:
            aCoins = coin_count.get(coin, 0)  
            while rest >= coin and aCoins > 0:
                rest -= coin  
                result.append(coin)  
                aCoins -= 1  
            
        if rest == 0:
            return result  
        else:
            return "Cannot give exact change with the available coins."  # If change can't be made


if __name__ == '__main__':
    totalSumForPaying = int(input("Enter the total sum: "))
    userSum = int(input("Enter the user sum: "))
    
    linkedList = SLL()
    coins = [10, 5, 2, 1] 
    for coin in coins:
        for i in range(100):  
            linkedList.insertNode(coin) 

    min_coins = atm(linkedList, totalSumForPaying, userSum)
        
    if isinstance(min_coins, list):
        print(f"The minimum coins you needed are: {min_coins}")
    else:
        print(min_coins)
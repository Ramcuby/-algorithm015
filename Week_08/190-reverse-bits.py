class Solution:
    def reverseBits(self, n: int) -> int:

        # return int('0b'+('0'*32+bin(n)[2:])[-32:][::-1], base=2)
        str1 = '0'*32+bin(n)[2:]  # 去掉’0b‘，补零
        str2 = '0b' + str1[-32:][::-1] # 取32位，倒序，增加’0b‘
        return int(str2,base=2)  # 按二进制返回

        
        # res = 0
        # for i in range(32):
        #     b=(n>>i)&1
        #     res=(res<<1)+b
        # return res
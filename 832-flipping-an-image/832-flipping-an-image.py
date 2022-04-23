class Solution:
    def rev(self, l):
        first = 0
        last = len(l) - 1
        while first < last:
            l[first], l[last] = l[last], l[first]
            first += 1
            last -= 1
        return l
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            self.rev(i)
        #print(image)
        #[[0,1,1], [0,1,0], [1,1,1]]
        for j in range(len(image)):#3
            for k in range(len(image[j])):#3
                if image[j][k] == 0:
                    image[j][k] = 1
                elif image[j][k] == 1:
                    image[j][k] = 0
        return image
                
        
        
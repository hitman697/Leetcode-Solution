class Sol(obj):
    def findMode(self, root):
        
        def order(root, prev, count, max_count, res):
            if not root:
                return prev, count, max_count

            prev, count, max_count = order(root.left, prev, count, max_count, res)
            if prev:
                if root.val == prev.val:
                    count += 1
                else:
                    count = 1
            if count > max_count:
                max_count = count
                del res[:]
                res.append(root.val)
            elif count == max_count:
                res.append(root.val)
            return order(root.right, root, count, max_count, res)

        if not root:
            return []
        res = []
        order(root, None, 1, 0, res)
        return res

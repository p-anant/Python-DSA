def xorQuery(queries):

   xor = 0

   new = []

   for i in range(len(queries)):

       if queries[i][0] == 1:

           new.append(queries[i][1] ^ xor)

       else:

           xor ^= queries[i][1]

   for i in range(len(new)):

       new[i] = new[i] ^ xor

   return new
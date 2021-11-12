#Let's make a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors
# n_neighbors on either side to consider. For each value, the function computes the average of each value's 
#neighbors, including themselves. Have the function return a list of these averaged values that is the same 
#length as the original list. If there are not enough neighbors (for cases near the edge), substitute the 
#original value as many times as there are missing neighbors.
#Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1

#The commented print functions were used to test the code

import statistics
def moving_window_average(x, n_neighbors):
    for n in range(0,len(x)):
        if (n-n_neighbors)<0 and (n+n_neighbors)>(len(x)-1):
          k1=-1*(n-n_neighbors)
          k2=n+n_neighbors-len(x)+1
          d1=[x[h] for h in range(0,len(x))]
          d1 += k2*[x[n]]
          d1 += k1*[x[n]]
        elif (n-n_neighbors)<0:
          k3=-1*(n-n_neighbors)
          d1=[x[h] for h in range(0,n+n_neighbors+1)]
          d1 += k3*[x[n]]
          #print(d1,k1)
        elif (n+n_neighbors)>(len(x)-1):
          k4=n+n_neighbors-len(x)+1
          d1=[x[h] for h in range(n-n_neighbors, len(x))]
          d1 += k4*[x[n]]
          #print(d1,k2)
        else:
          d1=[x[h] for h in range(n-n_neighbors,n+n_neighbors+1)]
          #print(d1)
        m = statistics.mean(d1)
        print(m)
        

moving_window_average([0,10,5,3,1,5],1)

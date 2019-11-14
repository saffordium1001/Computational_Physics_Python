#import Python libraries
import scipy as sci
import matplotlib.pyplot as plt

# Pick out any random 3D vector using sci.random.rand(1,3). This will yield a 3D vector centered around 0.5 with each coordinate having a value between 0 to 1.
# Subtract 0.5 from each coordinate so that it becomes centered around 0.
#Calculate the norm (or magnitude) of the vector and divide the vector by its norm ensuring that it becomes a unit vector. Any unit vector will necessarily lie on a sphere of radius 1.

points=10000 #Number of points 
x=sci.zeros((points,3)) #To store x-coordinates of sample points
y=sci.zeros((points,3)) #To store y-coordinates of sample pointsfor i in range(points):
    vector=sci.random.rand(1,3)-0.5
    if(sci.linalg.norm(vector)!=0 and sci.linalg.norm(vector)<=1.0):
        x[i,:]=vector
        y[i,:]=x[i,:]/sci.linalg.norm(x[i,:])
y_norms=sci.zeros(points) #Array to store norms of sample vectorsfor i in range(points):
    y_norms[i]=sci.linalg.norm(y[i,:])
    tol=1e-10 #Tolerance
    norm_diff=abs(y_norms-1) #Diff. between actual and desired norm
    danger_array=y_norms[norm_diff>tol]if(len(danger_array)==0): 
    print("All Clear")
else:
    print("Danger")

def CheckSide(vertices,point):
    t1,t2,t3,t4=vertices
    p=point
    side_1=t2-t1
    side_2=t3-t1
    normal=sci.cross(side_1,side_2)    ref_vector=t4-t1
    ref_sign=sci.dot(normal,ref_vector)    point_vector=p-t1
    point_sign=sci.dot(normal,point_vector)    if(sci.sign(ref_sign)==sci.sign(point_sign)):
        return 1
    else:
        return 0
   
def CheckTetrahedron(vertices,point):
    vert=sci.copy(vertices)
    check_1=CheckSide(vert,point)    vert=sci.roll(vert,1,axis=0)
    check_2=CheckSide(vert,point)    vert=sci.roll(vert,1,axis=0)
    check_3=CheckSide(vert,point)    vert=sci.roll(vert,1,axis=0)
    check_4=CheckSide(vert,point)    sum_check=check_1+check_2+check_3+check_4    if(sum_check==4.):
        return 1
    else:
        return 0
        
centre=[0,0,0]
number_of_samples=10000
sample_span=sci.arange(0,number_of_samples,1)
check_point=sci.zeros(number_of_samples) 
prob=sci.zeros(number_of_samples)

for i in range(number_of_samples):
    indices=sci.random.randint(0,points,4)
    vertex_list=y[indices]
    check_point[i]=CheckTetrahedron(vertex_list,centroid)
    prob[i]=len(check_point[check_point==1.])/(i+1)
    
#Plot blank figure
plt.figure(figsize=(15,10))#Plot resultant probability from simulation
plt.plot(sample_span,prob,color="navy",linestyle="-",label="Resultant probability from simulation")#Plot resultant probability from analytical solution
plt.plot(sample_span,[0.125]*len(sample_span),color="red",linestyle="-",label="Actual resultant probability from analytical solution (0.125)")#Plot value of final resultant probability in text
plt.text(sample_span[int(number_of_samples/2)],0.05,f"The final probability is {prob[-1]:.4f}",fontsize=16)#Display axis labels
plt.xlabel("Number of iterations",fontsize=14)
plt.ylabel("Probability",fontsize=14)#Display legend
plt.legend(loc="upper right",fontsize=14)#Display title of the plot
plt.title("Variation of resultant probability with increase in the number of iterations",fontsize=14)

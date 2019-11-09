// Wave2D.java: 2-D Wave eq for vibrating membrane

  import java.io.*; 
  
public class Wave2D { 
  final static double den =390.0, ten =180.0;    // Density, T, step
  
  public static void main(String[] argv) 
                  throws IOException, FileNotFoundException {
    int i, j, k;        // i,j: membrane grid positions, k: for time
    int max = 45;                       // Final time of oscillation
    double c, cprime, x, y;         // vel; cprime = delta u/delta t
    double covercp, incrx, incry;           // c, cprime, increments
    double u[][][] = new double[101][101][3];
    PrintWriter w =                       // Output in Helmholtz.dat
        new PrintWriter(new FileOutputStream("Helmholtz.dat"), true);
    double ratio;                                   // (c/cprime)^2.
    incrx = Math.PI/100.0;
    incry = Math.PI/100;
    c = Math.sqrt(ten/den);                     // Propagation speed
    cprime = c;                                    // For simplicity
    covercp = c/cprime;                                // c / cprime
    ratio = 0.5*covercp*covercp;                // 0.5 for stability
    System.out.println("ratio "+ratio);
    y = 0.0;
    for( j=0; j<101; j++ ) {          // Initial condition: position
      x = 0.0;
      for( i=0; i<101; i++ )  {
        u[i][j][0] = Math.sin(2.0*x)*Math.sin(y);
         x = x+incrx;
      }
      y = y+incry;
   }
   for ( j=1; j<100; j++ )  {                     // First time step
     for ( i=1; i<100; i++ )  {
       u[i][j][1] = u[i][j][0] +0.5*ratio*(u[i+1][j][0]+u[i-1][j][0]
            +u[i][j+1][0]+u[i][j-1][0]-4.0*u[i][j][0]) ;
     }
   }
   for ( k=1; k<=max; k++ )   {                       // Later times
     for ( j=1; j<100; j++ )  {
       for ( i=1; i<100; i++ )  {
         u[i][j][2] = 2.*u[i][j][1] - u[i][j][0]+ratio*(u[i+1][j][1]
         + u[i-1][j][1] + u[i][j+1][1]+u[i][j-1][1] - 4.*u[i][j][1]);
       }
     }
     for ( j=0; j<101; j++ ){
       for( i=0; i<101; i++ ){
         u[i][j][0] = u[i][j][1];                        // New past
         u[i][j][1] = u[i][j][2];                     // New present
       }
     }
     if ( k == max) {
       for ( j=0; j<101; j=j+2 ) {               // Last time values
         for( i=0; i<101; i=i+2 ) {
           w.println("  " +u[i][j][2] );
         }   //for gnuplot
         w.println("");
       }
     }                                                         // if
   }                                                 // for k (time)
   System.out.println("data stored in Helmholtz.dat");
 }
} 

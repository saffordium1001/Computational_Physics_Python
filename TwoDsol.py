#  TwoDsol.java: solves Sine-Gordon equation for 2D soliton 

import java.io.*; 
import java.util.*; 

public class TwoDsol {
  public static int D = 201; 
  public static double u[][][] = new double[D + 1][D + 1][4]; 

  public static void main(String[] argv) 
                        throws IOException, FileNotFoundException {                                          
    int nint; 
        // input positive integer proportional to time of wave packet
    Scanner sc = new Scanner(System.in);  // Connect Scanner to input
    System.out.printf("Enter a pos integer from 1 (initial time)\n"); 
    System.out.printf("to 100 for wave packet at that time:\n"); 
    nint = sc.nextInt();                                  // Read int
    initial(u);                                     // Initialization
    solution(u, nint);                              // Solve equation
  }

  public static void initial(double u[][][])  {
    double dx, dy, dt, xx, yy, dts, time, tmp; 
    int i, j, k; 
    dx = 14./200.; 
    dy = dx; 
    dt = dx/Math.sqrt(2.); 
    dts = (dt/dx)*(dt/dx); 
    yy = -7.; 
    time = 0.; 
    for ( i=0; i <= D-1; i++ )  {
      xx = -7.; 
      for ( j=0; j <= D-1; j++ )  {
        tmp = 3.-Math.sqrt(xx*xx + yy*yy); 
        u[i][j][0] = 4.*Math.atan(tmp); 
        xx = xx + dx; 
      }
      yy = yy + dy; 
  }  }
   
  public static void solution(double u[][][], int nint)
                          throws IOException, FileNotFoundException {
    PrintWriter w = 
            new PrintWriter(new FileOutputStream("2Dsol.dat"), true);
    double dx, dy, dt, time, a2, zz, dts, a1, tmp; 
    int l, m, mm, k, j, i; 
        
    dx = 14./200.; dy = dx; 
    dt = dx/Math.sqrt(2.); 
    time = 0.; 
    time = time + dt; 
    dts = (dt/dx)*(dt/dx); 
    tmp = 0.; 
    for ( m=1; m <= D-2; m++ )  {
      for ( l=1; l <= D-2; l++ )  {
        a2 = u[m+1][l][0]+u[m-1][l][0] + u[m][l+1][0] + u[m][l-1][0];
        tmp = .25*a2; 
        u[m][l][1] = 0.5*(dts*a2-dt*dt*Math.sin(tmp)); 
      }
    } 
    for ( mm=1; mm <= D-2; mm++ )  {   // Borders in second iteration
      u[mm][0][1] = u[mm][1][1]; 
      u[mm][D-1][1] = u[mm][D-2][1]; 
      u[0][mm][1] = u[1][mm][1]; 
      u[D-1][mm][1] = u[D-2][mm][1]; 
    }
    u[0][0][1] = u[1][0][1];                 // Still undefined terms
    u[D-1][0][1] = u[D-2][0][1]; 
    u[0][D-1][1] = u[1][D-1][1]; 
    u[D-1][D-1][1] = u[D-2][D-1][1]; 
    tmp = 0.;   
    for ( k=0; k <= nint; k++ )  {            // Following iterations
      for ( m=1; m <= D-2; m++ )  {
        for ( l=1; l <= D-2; l++ )  {
          a1 = u[m + 1][l][1]+u[m-1][l][1]+u[m][l+1][1]+u[m][l-1][1];
          tmp = .25*a1; 
          u[m][l][2] = -u[m][l][0] + dts*a1-dt*dt*Math.sin(tmp); 
          u[m][0][2] = u[m][1][2]; 
          u[m][D-1][2] = u[m][D-2][2]; 
      } }
      for ( mm=1; mm <= D-2; mm++ )  {
        u[mm][0][2] = u[mm][1][2]; 
        u[mm][D-1][2] = u[mm][D-2][2]; 
        u[0][mm][2] = u[1][mm][2]; 
        u[D-1][mm][2] = u[D-2][mm][2]; 
      }
      u[0][0][2] = u[1][0][2]; 
      u[D-1][0][2] = u[D-2][0][2]; 
      u[0][D-1][2] = u[1][D-1][2]; 
      u[D-1][D-1][2] = u[D-2][D-1][2];            
      for ( l=0; l <= D-1; l++ )  {            // New iterations now old 
        for ( m=0; m <= D-1; m++ )  {
          u[l][m][0] = u[l][m][1]; 
          u[l][m][1] = u[l][m][2]; 
        }
      }
      if (k==nint) {
        for ( i=0; i <= D-1; i=i + 5)  {
          for ( j=0; j <= D-1; j=j + 5) 
            { w.println("" + (float)Math.sin(u[i][j][2]/2.) + ""); }
          w.println("  "); 
}  }
      time = time + dt; 
}  }  } 

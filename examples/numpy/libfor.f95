subroutine tridiag_rpkw(nodes, weights, alpha, beta, n)
   implicit none

   ! Argument variables
   integer, intent(in) :: n
   double precision, intent(in) :: nodes(n), weights(n)
   double precision, intent(inout) :: alpha(n), beta(n)

   ! Auxilliary variables
   double precision :: pi2, lam, gamma2, sigma2, tau, rho2
   double precision :: oldBeta, oldSigma2, newTau

   ! Loop indexes
   integer :: i, k

   ! Intialize alpha, beta
   do i=1,n
      alpha(i) = nodes(i)
      beta(i) = 0.
   end do
   beta(1) = weights(1)

   ! Loop on each submatrices of the arrow matrix
   do i=1,n-1

      pi2 = weights(i+1)
      lam = nodes(i+1)

      gamma2 = 1.
      sigma2 = 1.
      tau = 0.

      ! Apply rotations successively to tridiagonalize the submatrix
      do k=1,i+1

         oldBeta = beta(k)
         rho2 = oldBeta + pi2
         beta(k) = gamma2*rho2
         oldSigma2 = sigma2

         if (rho2 <= 0.) then
            gamma2 = 1.
            sigma2 = 0.
         else
            gamma2 = oldBeta/rho2
            sigma2 = pi2/rho2
         end if

         newTau = sigma2*(alpha(k)-lam) - gamma2*tau
         alpha(k) = alpha(k) - (newTau-tau)
         tau = newTau

         if (sigma2 <= 0.) then
            pi2 = oldSigma2*beta(k)
         else
            pi2 = tau**2/sigma2
         end if

      end do

   end do

end subroutine
#include <iostream>
#include <cmath>

class Complex{
  public:
    Complex(double r=0.0,double i=0.0):re(r),im(i){}
    friend Complex operator-(const Complex& z){
      Complex s;
      s.re=-z.re;
      s.im=-z.im;
      return s;
    }
    friend Complex operator+(const Complex& z1,const Complex& z2){
      Complex s;
      s.re=z1.re+z2.re;
      s.im=z1.im+z2.im;
      return s;
    }
    friend Complex operator-(const Complex& z1,const Complex& z2){
      Complex s;
      s.re=z1.re-z2.re;
      s.im=z1.im-z2.im;
      return s;
    }
    friend Complex operator*(const Complex& z1,const Complex& z2){
      Complex s;
      s.re=z1.re*z2.re-z1.im*z2.im;
      s.im=z1.re*z2.im+z1.im*z2.re;
      return s;
    }
    friend Complex operator/(const Complex& z1,const Complex& z2){
      Complex s;
      double r=z2.re*z2.re+z2.im*z2.im;
      s.re=(z1.re*z2.re+z1.im*z2.im)/r;
      s.im=(-z1.re*z2.im+z1.im*z2.re)/r;
      return s;
    }
    friend double abs(const Complex& z){
      return std::sqrt(z.re*z.re+z.im*z.im);
    }
  private:
    double re,im;
};

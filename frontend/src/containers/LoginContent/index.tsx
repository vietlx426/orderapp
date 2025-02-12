"use client"

import { useState } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Eye, EyeOff } from "lucide-react"
import Image from "next/image"
import Link from "next/link"
import LoginImage from "../../../public/images/loginicon.jpg"

export default function LoginContent() {
  const [showPassword, setShowPassword] = useState(false)

  return (
    <div className="flex flex-col md:flex-row">
      {/* Left side with illustration */}
      <div className="w-full md:w-1/2 bg-[#FFE7DF] flex items-center justify-center">
        <div className="relative w-full aspect-square max-w-[400px]">
          <Image
            src={LoginImage || "/placeholder.svg"}
            alt="Moofitask Mascot"
            fill
            className="object-cover object-center"
            priority
          />
        </div>
      </div>

      {/* Right side with login form */}
      <div className="w-full md:w-1/2 p-8 md:p-12 lg:p-16">
        <div className="max-w-sm mx-auto">
          {/* Logo */}
          <h1 className="text-2xl font-bold mb-2 text-[#FF5757]">OU order food</h1>

          {/* Login Form */}
          <div className="mt-8">
            <h2 className="text-2xl font-semibold mb-8">Login</h2>
            <form className="space-y-6">
              <div className="space-y-2">
                <label className="text-sm font-medium text-gray-700">Email</label>
                <Input type="email" placeholder="name@example.com" className="rounded-xl border-gray-200" />
              </div>

              <div className="space-y-2">
                <div className="flex justify-between">
                  <label className="text-sm font-medium text-gray-700">Password</label>
                  <Link href="/forgot-password" className="text-sm text-[#FF5757] hover:text-[#FF3333]">
                    Forgot Password?
                  </Link>
                </div>
                <div className="relative">
                  <Input
                    type={showPassword ? "text" : "password"}
                    placeholder="••••••••"
                    className="rounded-xl border-gray-200 pr-10"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500"
                  >
                    {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                  </button>
                </div>
              </div>

              <Button type="submit" className="w-full bg-[#FF5757] hover:bg-[#FF3333] text-white rounded-xl py-2.5">
                Log in
              </Button>
            </form>

            {/* Divider */}
            <div className="relative my-6">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-200"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-2 bg-white text-gray-500">Or Continue With</span>
              </div>
            </div>

            {/* Social Login */}
            <div className="grid grid-cols-1 gap-1">
              <Button variant="outline" className="rounded-xl border-gray-200">
                <Image src="/google.svg" alt="Google" width={20} height={20} />
              </Button>
            </div>

            {/* Sign Up Link */}
            <p className="mt-8 text-center text-sm text-gray-600">
              Don't have an account?{" "}
              <Link href="/Dashboard" className="text-[#FF5757] hover:text-[#FF3333] font-medium">
                Sign Up here
              </Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}


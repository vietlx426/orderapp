"use client"

import { useState, useEffect } from "react"
import dynamic from "next/dynamic"
import LoginSkeleton from "./loading"

const LoginContent = dynamic(() => import("./../containers/LoginContent"), {
  loading: () => <LoginSkeleton />,
})

export default function LoginPage() {
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 1000)

    return () => clearTimeout(timer)
  }, [])

  return (
    <div className="min-h-screen w-full bg-pink-50/50 flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl shadow-xl w-full max-w-4xl overflow-hidden">
        {isLoading ? <LoginSkeleton /> : <LoginContent />}
      </div>
    </div>
  )
}

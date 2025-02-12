import { Skeleton } from "@/components/ui/skeleton"

export default function LoginSkeleton() {
  return (
    <div className="flex flex-col md:flex-row">
      {/* Left side illustration skeleton */}
      <div className="w-full md:w-1/2 bg-[#FFE7DF] flex items-center justify-center p-8">
        <Skeleton className="w-full aspect-square max-w-[400px] rounded-2xl bg-[#FFE7DF]" />
      </div>

      {/* Right side form skeleton */}
      <div className="w-full md:w-1/2 p-8 md:p-12 lg:p-16">
        <div className="max-w-sm mx-auto">
          {/* Logo skeleton */}
          <Skeleton className="h-8 w-32 mb-2 bg-[#FFE7DF]/20" />

          <div className="mt-8">
            {/* Title skeleton */}
            <Skeleton className="h-8 w-24 mb-8" />

            {/* Form skeletons */}
            <div className="space-y-6">
              {/* Email field */}
              <div className="space-y-2">
                <Skeleton className="h-4 w-12" />
                <Skeleton className="h-10 w-full rounded-xl" />
              </div>

              {/* Password field */}
              <div className="space-y-2">
                <div className="flex justify-between">
                  <Skeleton className="h-4 w-16" />
                  <Skeleton className="h-4 w-28 bg-[#FF5757]/20" />
                </div>
                <Skeleton className="h-10 w-full rounded-xl" />
              </div>

              {/* Login button skeleton */}
              <Skeleton className="h-10 w-full rounded-xl bg-[#FF5757]/20" />
            </div>

            {/* Divider skeleton */}
            <div className="relative my-6">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-200"></div>
              </div>
              <div className="relative flex justify-center">
                <Skeleton className="h-4 w-32 bg-white" />
              </div>
            </div>

            {/* Social login skeletons */}
            <div className="grid grid-cols-1 gap-1">
              <Skeleton className="h-10 w-full rounded-xl" />
            </div>

            {/* Sign up link skeleton */}
            <div className="mt-8 flex items-center justify-center gap-2">
              <Skeleton className="h-4 w-32" />
              <Skeleton className="h-4 w-20 bg-[#FF5757]/20" />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}


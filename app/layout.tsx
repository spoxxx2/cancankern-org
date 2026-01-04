import "./globals.css"
import { Geist, Geist_Mono } from "@next/font-geist"
import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "CANCAN Admin",
  description: "CANCAN Admin Panel",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${Geist.variable} ${Geist_Mono.variable}`}>
      <body>{children}</body>
    </html>
  )
}


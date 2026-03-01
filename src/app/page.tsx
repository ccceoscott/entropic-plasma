import Image from "next/image";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Rocket, Shield, Zap } from "lucide-react";

export default function Home() {
  return (
    <main className="min-h-screen bg-background py-12 md:py-24 p-4 md:p-8 flex flex-col items-center">
      <div className="max-w-4xl w-full flex flex-col gap-8 md:gap-12">

        {/* Header Section */}
        <section className="flex flex-col gap-3 text-center items-center">
          <h1 className="text-3xl font-bold tracking-tight lg:text-4xl">
            Entropic Plasma Prototype
          </h1>
          <p className="max-w-xl text-base text-muted-foreground">
            A Next.js 15 application explicitly designed strictly following the Infinity Protocol and the 4px Spacing Grid rules.
          </p>
          <div className="flex gap-3 mt-4">
            <Button className="bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 rounded-md focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
              Start Project
            </Button>
            <Button variant="outline" className="bg-secondary text-secondary-foreground hover:bg-secondary/80 h-10 px-4 py-2 rounded-md focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
              Read Docs
            </Button>
          </div>
        </section>

        {/* Feature Cards Section */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card className="border border-border shadow-sm rounded-xl bg-card text-card-foreground">
            <CardHeader className="gap-2">
              <Zap className="h-6 w-6 text-primary" />
              <CardTitle className="text-xl font-semibold tracking-tight">Lightning Fast</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription className="text-sm text-muted-foreground">
                Built on Next.js App Router for maximum performance and React Server Components.
              </CardDescription>
            </CardContent>
            <CardFooter>
              <Button variant="ghost" className="w-full text-sm hover:bg-accent focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
                Learn More
              </Button>
            </CardFooter>
          </Card>

          <Card className="border border-border shadow-sm rounded-xl bg-card text-card-foreground">
            <CardHeader className="gap-2">
              <Shield className="h-6 w-6 text-primary" />
              <CardTitle className="text-xl font-semibold tracking-tight">Secure by Default</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription className="text-sm text-muted-foreground">
                Following the Infinity Protocol's strict locks for complete deployment safety.
              </CardDescription>
            </CardContent>
            <CardFooter>
              <Button variant="ghost" className="w-full text-sm hover:bg-accent focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
                Learn More
              </Button>
            </CardFooter>
          </Card>

          <Card className="border border-border shadow-sm rounded-xl bg-card text-card-foreground">
            <CardHeader className="gap-2">
              <Rocket className="h-6 w-6 text-primary" />
              <CardTitle className="text-xl font-semibold tracking-tight">Production Ready</CardTitle>
            </CardHeader>
            <CardContent>
              <CardDescription className="text-sm text-muted-foreground">
                Fully pre-configured with Tailwind, shadcn/ui, and standard typography structures.
              </CardDescription>
            </CardContent>
            <CardFooter>
              <Button variant="ghost" className="w-full text-sm hover:bg-accent focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
                Learn More
              </Button>
            </CardFooter>
          </Card>
        </section>

      </div>
    </main>
  );
}

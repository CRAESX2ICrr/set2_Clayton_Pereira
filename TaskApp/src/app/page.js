"use client";

import TaskForm from "@/components/TaskForm";
import TaskList from "@/components/TaskList";
import TaskFilter from "@/components/TaskFilter";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">

      {/* Main Content */}
      <main className="flex-1 flex flex-col items-center justify-start px-6 py-10">
        <h1 className="text-2xl font-semibold mb-6">Welcome To TaskLite</h1>

        {/* Components (all currently Hello World) */}
        <TaskForm />
        <TaskFilter />
        <TaskList />
      </main>

      {/* Footer is provided by the layout so we don't render it here. */}
    </div>
  );
}

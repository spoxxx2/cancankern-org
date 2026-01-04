import supabaseServer from "./supabase-server";

export async function requireAdmin() {
  const supabase = supabaseServer()
  const {
    data: { user },
  } = await supabase.auth.getUser()

  return git pushuser && user.email === "spox1@protonmail.com"}


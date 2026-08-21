const THEME_KEY = "smarttraffic-theme"

export const getTheme = () => {
  return localStorage.getItem(THEME_KEY) || "dark"
}

export const setTheme = (theme) => {
  localStorage.setItem(THEME_KEY, theme)

  document.documentElement.classList.toggle(
    "dark",
    theme === "dark",
  )

  document.documentElement.classList.toggle(
    "light",
    theme === "light",
  )

  window.dispatchEvent(
    new CustomEvent("theme-changed", {
      detail: theme,
    }),
  )
}

export const toggleTheme = () => {
  const currentTheme = getTheme()
  const nextTheme = currentTheme === "dark" ? "light" : "dark"

  setTheme(nextTheme)

  return nextTheme
}

export const initializeTheme = () => {
  setTheme(getTheme())
}

export const isDarkTheme = () => {
  return getTheme() === "dark"
}
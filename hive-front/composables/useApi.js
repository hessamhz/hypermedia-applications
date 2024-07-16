// Utility function for making API calls using useFetch
export function useApi(path, options = {}) {
  const config = useRuntimeConfig();
  return useFetch(`${path}`, {
    ...options, // Merge the provided options with the defaults
    baseURL: config.public.baseURL, // Use the base URL from the public runtime configuration
  });
}

const API_BASE_URL = "http://localhost:8000"

const request = async (endpoint, options = {}) => {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  })

  if (!response.ok) {
    const errorData = await response.json().catch(() => null)

    throw new Error(
      errorData?.detail || `Request failed with status ${response.status}`,
    )
  }

  return response.json()
}

export const getCameras = () => {
  return request("/api/cameras/")
}

export const getTrafficData = (params = {}) => {
  const searchParams = new URLSearchParams()

  if (params.camera_id) {
    searchParams.append("camera_id", params.camera_id)
  }

  if (params.start_time) {
    searchParams.append("start_time", params.start_time)
  }

  if (params.end_time) {
    searchParams.append("end_time", params.end_time)
  }

  const queryString = searchParams.toString()

  return request(
    `/api/traffic/${queryString ? `?${queryString}` : ""}`,
  )
}

export const getTrafficStatistics = (params = {}) => {
  const searchParams = new URLSearchParams()

  if (params.camera_id) {
    searchParams.append("camera_id", params.camera_id)
  }

  if (params.start_time) {
    searchParams.append("start_time", params.start_time)
  }

  if (params.end_time) {
    searchParams.append("end_time", params.end_time)
  }

  const queryString = searchParams.toString()

  return request(
    `/api/traffic/statistics${queryString ? `?${queryString}` : ""}`,
  )
}

export const getAlerts = (params = {}) => {
  const searchParams = new URLSearchParams()

  if (params.camera_id) {
    searchParams.append("camera_id", params.camera_id)
  }

  if (params.severity) {
    searchParams.append("severity", params.severity)
  }

  const queryString = searchParams.toString()

  return request(
    `/api/alerts/${queryString ? `?${queryString}` : ""}`,
  )
}

export const getPredictions = (cameraId = "") => {
  const searchParams = new URLSearchParams()

  if (cameraId) {
    searchParams.append("camera_id", cameraId)
  }

  const queryString = searchParams.toString()

  return request(
    `/api/predictions/${queryString ? `?${queryString}` : ""}`,
  )
}
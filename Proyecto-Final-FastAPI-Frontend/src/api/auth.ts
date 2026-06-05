import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  RegisterResponse,
  ErrorResponse,
} from "../types/auth";

export const loginUser = async (data: LoginRequest): Promise<LoginResponse> => {
  const res = await fetch("http://192.168.64.2/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const result = await res.json();

  if (!res.ok) {
    const err = result as ErrorResponse;
    throw new Error(err.detail || "Error en login");
  }

  return result as LoginResponse;
};

export const registerUser = async (
  data: RegisterRequest,
): Promise<RegisterResponse> => {
  const res = await fetch("http://192.168.64.2/api/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const result = await res.json();

  if (!res.ok) {
    const err = result as ErrorResponse;
    throw new Error(err.detail || "Error en registro");
  }

  return result as RegisterResponse;
};

import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  RegisterResponse,
  ErrorResponse,
} from "../types/auth";

export const loginUser = async (data: LoginRequest): Promise<LoginResponse> => {
  const res = await fetch("http://127.0.0.1:8000/login", {
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
  const res = await fetch("http://127.0.0.1:8000/register", {
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

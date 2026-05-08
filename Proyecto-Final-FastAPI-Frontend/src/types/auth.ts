// 🔐 Base (reutilizable)
export type AuthRequest = {
  username: string;
  password: string;
};

// 📥 Requests
export type LoginRequest = AuthRequest;
export type RegisterRequest = AuthRequest;

// 📤 Responses
export type LoginResponse = {
  message: string;
  username: string;
};

export type RegisterResponse = {
  message: string;
  username: string;
};

// ❌ Errores (FastAPI)
export type ErrorResponse = {
  detail: string;
};

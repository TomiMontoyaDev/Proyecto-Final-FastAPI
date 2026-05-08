import { useState } from "react";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { registerUser } from "../api/auth";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleRegister = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await registerUser({ username, password });
      console.log(res);

      // opcional: feedback
      alert("Usuario registrado con exito!");
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
      navigate("/");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-black">
      {/* 🔥 Background gradient blobs */}
      <div className="absolute w-[500px] h-[500px] bg-purple-600 rounded-full blur-3xl opacity-30 top-[-100px] left-[-100px]" />
      <div className="absolute w-[400px] h-[400px] bg-blue-600 rounded-full blur-3xl opacity-30 bottom-[-100px] right-[-100px]" />

      {/* 💎 Card */}
      <motion.div
        initial={{ opacity: 0, scale: 0.9, y: 40 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="relative z-10 w-[360px] p-8 rounded-3xl 
        bg-white/10 backdrop-blur-xl border border-white/20 
        shadow-[0_0_40px_rgba(0,0,0,0.6)]"
      >
        {/* 🧠 Title */}
        <h1 className="text-3xl font-extrabold text-white text-center mb-2">
          Crear cuenta
        </h1>
        <p className="text-gray-300 text-center mb-6 text-sm">Registro</p>

        {/* 👤 Username */}
        <motion.input
          whileFocus={{ scale: 1.03 }}
          type="text"
          placeholder="Usuario"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full mb-4 px-4 py-3 rounded-xl 
          bg-white/20 text-white placeholder-gray-300 
          outline-none focus:ring-2 focus:ring-purple-500 
          transition-all duration-300"
        />

        {/* 🔒 Password */}
        <motion.input
          whileFocus={{ scale: 1.03 }}
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full mb-4 px-4 py-3 rounded-xl 
          bg-white/20 text-white placeholder-gray-300 
          outline-none focus:ring-2 focus:ring-blue-500 
          transition-all duration-300"
        />

        {/* ⚠️ Error */}
        {error && (
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-red-400 text-sm text-center mb-3"
          >
            {error}
          </motion.p>
        )}

        {/* 🚀 Button */}
        <motion.button
          whileTap={{ scale: 0.95 }}
          whileHover={{ scale: 1.03 }}
          onClick={handleRegister}
          disabled={loading}
          className="w-full py-3 rounded-xl font-semibold text-white
          bg-gradient-to-r from-purple-500 via-blue-500 to-cyan-500
          hover:opacity-90 transition-all duration-300 
          shadow-lg shadow-blue-500/30"
        >
          {loading ? "Registrando..." : "Registrarse"}
        </motion.button>

        {/* ✨ Extra */}
        <p className="text-gray-400 text-xs text-center mt-4">
          ¿Ya tienes cuenta?{" "}
          <Link to="/">
            <span className="text-blue-400 cursor-pointer">Iniciar Sesion</span>
          </Link>
        </p>
      </motion.div>
    </div>
  );
}

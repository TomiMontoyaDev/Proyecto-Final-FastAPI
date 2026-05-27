import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";

export default function Profile() {
  const [userData, setUserData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        navigate("/");
        return;
      }

      try {
        const res = await fetch("http://127.0.0.1:8000/protected", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!res.ok) {
          throw new Error("Error al obtener el perfil o token expirado");
        }

        const data = await res.json();
        setUserData(data);
      } catch (err: any) {
        setError(err.message);
        localStorage.removeItem("token");
        localStorage.removeItem("user");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/");
  };

  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-black text-white p-4">
      {/* 🔥 Background gradient blobs */}
      <div className="absolute w-[500px] h-[500px] bg-cyan-600 rounded-full blur-3xl opacity-20 top-[-100px] left-[-100px]" />
      <div className="absolute w-[400px] h-[400px] bg-blue-600 rounded-full blur-3xl opacity-20 bottom-[-100px] right-[-100px]" />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="relative z-10 w-full max-w-2xl p-8 rounded-3xl 
        bg-white/10 backdrop-blur-xl border border-white/20 
        shadow-[0_0_40px_rgba(0,0,0,0.6)]"
      >
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
            Perfil de Usuario
          </h1>
          <button
            onClick={handleLogout}
            className="px-4 py-2 rounded-xl bg-red-500/20 border border-red-500/50 hover:bg-red-500/40 transition-all text-sm font-semibold"
          >
            Cerrar Sesión
          </button>
        </div>

        {loading ? (
          <p className="text-center text-gray-400 animate-pulse">Cargando datos...</p>
        ) : error ? (
          <div className="text-center">
            <p className="text-red-400 mb-4">{error}</p>
            <button onClick={() => navigate("/")} className="text-blue-400 underline">Volver al login</button>
          </div>
        ) : (
          <div className="space-y-4">
            <div className="p-4 rounded-2xl bg-black/40 border border-white/10">
              <p className="text-gray-400 text-sm mb-1">Mensaje del servidor:</p>
              <p className="text-green-400 font-medium">{userData.message}</p>
            </div>

            <div className="p-4 rounded-2xl bg-black/40 border border-white/10">
              <p className="text-gray-400 text-sm mb-2">Datos del JWT (JSON):</p>
              <pre className="text-xs md:text-sm font-mono overflow-x-auto text-cyan-300 p-2">
                {JSON.stringify(userData.user_info, null, 2)}
              </pre>
            </div>
          </div>
        )}

        <div className="mt-8 pt-6 border-t border-white/10 text-center">
            <img src="/logohardsoft.png" alt="Logo Hardsoft" className="h-8 mx-auto opacity-50" />
        </div>
      </motion.div>
    </div>
  );
}

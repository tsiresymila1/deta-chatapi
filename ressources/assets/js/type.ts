export interface IUser {
  id: string;
  name: string;
  username: string,
  role: string;
  email: string;
  password: string;
  profile?: File
}
